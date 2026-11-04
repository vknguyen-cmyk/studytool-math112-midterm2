"""Crop exact regions (an item from its label to the next label) out of the source PDFs."""
import re, subprocess, html, os, functools
from PIL import Image, ImageChops

SRC = "/home/claude/src/Math 112 Midterm 2"
FILES = {
 "L9":"MATH 112 Lecture 9","L10":"MATH 112 Lecture 10","L11":"MATH 112 Lecture 11","L12":"MATH 112 Lecture 12",
 "L13":"MATH 112 Lecture 13","L14":"MATH 112 Lecture 14","L15":"MATH 112 Lecture 15 (1)","L16":"MATH 112 Lecture 16",
 "HW5":"Math 112 Homework 5 (1)","HW6":"Math 112 Homework 6","HW7":"Math 112 Homework 7","HW8":"Math 112 Homework 8","HW9":"Math 112 Homework 9",
 "PA":"Practice Exam 2A","PB":"Practice Exam 2B",
}
DPI = 170
LEC_ANCHOR = re.compile(r"^(Definition|Theorem|Proposition|Remark|Example|Exercise|Examples|Question|Proof template|Properties|Geometric (meaning|interpretation)|Same points|Predicting limits|Additional practice|Graphing sequences|Completeness axiom)\b|^\d+(\.\d+)?\s+[A-Z][a-z]|^(\d+\s+)?(Bounded sequences|Comparison and Squeeze|Algebra of limits|Geometric sequence|Sequences$|Some other basic|Root and ratio|Divergence to infinity|Uniqueness of limit|Triangle inequality$)")
PROB_ANCHOR = re.compile(r"^(Problem\s*\d|Assignment \d|Special-angle reference)")
PART_ANCHOR = re.compile(r"^\(\s?[a-h]\s?\)\s|^\d\.\s+[A-Z]")

def pdfpath(fk): return f"{SRC}/{FILES[fk]}.pdf"

@functools.lru_cache(None)
def lines(fk):
    out = subprocess.run(["pdftotext","-bbox-layout",pdfpath(fk),"-"],capture_output=True,text=True).stdout
    res=[]; page=0; ph=792
    for m in re.finditer(r'<page width="([\d.]+)" height="([\d.]+)">|<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', out, re.S):
        if m.group(1): page+=1; ph=float(m.group(2)); continue
        words = re.findall(r'<word[^>]*>([^<]*)</word>', m.group(7))
        t = html.unescape(" ".join(words)).strip()
        x0,y0,x1,y1 = map(float,m.group(3,4,5,6))
        res.append(dict(page=page,x0=x0,y0=y0,x1=x1,y1=y1,t=t,ph=ph))
    res.sort(key=lambda l:(l["page"], round(l["y0"]/3), l["x0"]))
    # merge a lone section number with its heading text on the same baseline
    merged=[]
    for l in res:
        if merged and re.fullmatch(r"\d+(\.\d+)?", merged[-1]["t"]) and merged[-1]["page"]==l["page"] and abs(merged[-1]["y0"]-l["y0"])<4 and l["x0"]>merged[-1]["x1"]:
            m0=merged[-1]; m0["t"]=m0["t"]+" "+l["t"]; m0["x1"]=l["x1"]; m0["y1"]=max(m0["y1"],l["y1"]); continue
        merged.append(l)
    res=merged
    # mark header/footer
    for l in res:
        l["hf"] = bool(l["y0"]<100 and re.match(r"^(Math 112|MATH 112)\b|^Lecture \d+|^[A-Z][a-z]{2} \d{1,2}, 20\d\d$", l["t"])) \
                  or (re.fullmatch(r"\d{1,2}", l["t"]) and l["y0"]>l["ph"]-90) \
                  or (re.match(r"^Math 112 Midterm", l["t"]))
    return res

def find(fk, pats, after=None):
    """Find line index matching each regex in sequence."""
    L = lines(fk); i = -1 if after is None else after
    for p in pats:
        rx = re.compile(p)
        i = next((k for k in range(i+1,len(L)) if not L[k]["hf"] and rx.search(L[k]["t"])), None)
        if i is None: raise ValueError(f"{fk}: no match for {p!r}")
    return i

def region(fk, start_pats, end="auto", level="lec"):
    L = lines(fk); s = find(fk, start_pats)
    if end == "auto":
        rx = {"lec":LEC_ANCHOR,"prob":PROB_ANCHOR,"part":re.compile(PART_ANCHOR.pattern+"|"+PROB_ANCHOR.pattern)}[level]
        e = next((k for k in range(s+1,len(L)) if not L[k]["hf"] and rx.search(L[k]["t"])), len(L))
    else:
        try: e = find(fk, [end], after=s)
        except ValueError: e = len(L)
    return s, e

@functools.lru_cache(None)
def page_img(fk, page):
    path=f"/home/claude/build/pgcache/{fk}_{page}.png"
    if not os.path.exists(path):
        os.makedirs("/home/claude/build/pgcache",exist_ok=True)
        subprocess.run(["pdftoppm","-r",str(DPI),"-png","-gray","-f",str(page),"-l",str(page),"-singlefile",pdfpath(fk),path[:-4]],check=True)
    return Image.open(path).convert("L")

def trim(im):
    bg = Image.new("L", im.size, 255); diff = ImageChops.difference(im, bg).point(lambda v: 255 if v>40 else 0)
    bb = diff.getbbox()
    if not bb: return None
    return im.crop((max(0,bb[0]-6), max(0,bb[1]-6), min(im.width,bb[2]+6), min(im.height,bb[3]+6)))

def crop(fk, start_pats, end="auto", level="lec", out=None, tight=False):
    L = lines(fk); s, e = region(fk, start_pats, end, level)
    k = 2 if fk.startswith("L") else 1
    pieces=[]; pages = sorted({L[i]["page"] for i in range(s, e)} if e> s else {L[s]["page"]})
    if e < len(L) and L[e]["page"] > L[s]["page"] and e-1>=s:
        pages = list(range(L[s]["page"], L[e]["page"]+1))
    for pg in pages:
        body = [l for l in L if l["page"]==pg and not l["hf"]]
        def band(a):  # include fraction/superscript fragments that overlap the anchor line
            return min([a["y0"]]+[l["y0"] for l in body if l["y1"]>a["y0"]+1.5 and l["y0"]<a["y0"] and a["y0"]-l["y0"]<12])
        top = band(L[s])-3 if pg==L[s]["page"] else min(l["y0"] for l in body)-3
        if e < len(L) and L[e]["page"]==pg:
            bot = band(L[e])-2
            if tight: bot = max(l["y1"] for l in body if top < l["y0"] < bot) + 3
        else:
            foot = [l for l in L if l["page"]==pg and l["hf"] and l["y0"]>400]
            bot = (min(l["y0"] for l in foot)-2) if foot else body[-1]["ph"]-40
        if bot <= top: continue
        im = page_img(fk, pg); sc = im.height/ L[s]["ph"]
        xs = [l["x0"] for l in L if not l["hf"]]; xe=[l["x1"] for l in L if not l["hf"]]
        x0 = max(0, min(xs)-8); x1 = min(612, max(xe)+8)
        c = trim(im.crop((int(x0*sc), int(top*sc), int(x1*sc), int(bot*sc))))
        if c: pieces.append(c)
    W = max(p.width for p in pieces); H = sum(p.height for p in pieces) + 16*(len(pieces)-1)
    canvas = Image.new("L", (W,H), 255); y=0
    for p in pieces: canvas.paste(p,(0,y)); y+=p.height+16  # pieces left-aligned
    if out: canvas.save(out, optimize=True)
    return canvas, L[s]["page"], " ".join(L[i]["t"] for i in range(s, min(e,len(L))) if not L[i]["hf"])

def crop_multi(fk, segs, out):
    parts=[crop(fk, *seg) for seg in segs]
    W=max(p[0].width for p in parts); H=sum(p[0].height for p in parts)+10*(len(parts)-1)
    c=Image.new("L",(W,H),255); y=0
    for p in parts: c.paste(p[0],(0,y)); y+=p[0].height+10
    c.save(out, optimize=True)
    return c, parts[0][1], " ".join(p[2] for p in parts)
def _unused():
    return canvas, L[s]["page"], " ".join(L[i]["t"] for i in range(s, min(e,len(L))) if not L[i]["hf"])
