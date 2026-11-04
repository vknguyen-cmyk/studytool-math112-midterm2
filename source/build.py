import json, re, sys, os, shutil, glob
sys.path.insert(0, os.path.dirname(__file__))
from items import L
from goals import G, RECHECK

SRC = "/home/claude/src/Math 112 Midterm 2"
PAGES = "/home/claude/build/pages"
FILES = {
 "L9":("MATH 112 Lecture 9","Lecture 9"),"L10":("MATH 112 Lecture 10","Lecture 10"),"L11":("MATH 112 Lecture 11","Lecture 11"),
 "L12":("MATH 112 Lecture 12","Lecture 12"),"L13":("MATH 112 Lecture 13","Lecture 13"),"L14":("MATH 112 Lecture 14","Lecture 14"),
 "L15":("MATH 112 Lecture 15 (1)","Lecture 15"),"L16":("MATH 112 Lecture 16","Lecture 16"),
 "HW5":("Math 112 Homework 5 (1)","Homework 5"),"HW6":("Math 112 Homework 6","Homework 6"),"HW7":("Math 112 Homework 7","Homework 7"),
 "HW8":("Math 112 Homework 8","Homework 8"),"HW9":("Math 112 Homework 9","Homework 9"),
 "P8":("PCRQ 8","PCRQ 8"),"P9":("PCRQ 9","PCRQ 9"),"P10":("PCRQ 10","PCRQ 10"),"P11":("PCRQ 11","PCRQ 11"),"P12":("PCRQ 12","PCRQ 12"),"P14":("PCRQ 14","PCRQ 14"),
 "PA":("Practice Exam 2A","Practice Exam 2A"),"PB":("Practice Exam 2B","Practice Exam 2B"),
}
ETPAGE = {"9":7,"10":6,"11":5,"12":4,"13":2,"14":1,"15":3}
KIND = lambda k: "lecture" if k.startswith("L") else "homework" if k.startswith("HW") else "pcrq" if k.startswith("P") and k[1:].isdigit() else "exam" if k in("PA","PB") else "ticket"

def norm(s): return re.sub(r"\s+"," ",s.replace("’","'").replace("ﬁ","fi")).strip()
cache = {}
def pages(fk):
    if fk not in cache:
        base = FILES[fk][0]; out=[]
        for p in sorted(glob.glob(f"{PAGES}/{glob.escape(base)}__*.txt"), key=lambda x:int(x.rsplit("__",1)[1][:-4])):
            out.append(norm(open(p).read()))
        cache[fk]=out
    return cache[fk]

items = {}; miss=[]
for iid,(fk,label,needle,text) in L.items():
    if fk=="ET":
        lec = iid[2:].split(".")[0]; page=ETPAGE[lec]; src="Exit Tickets"; file="pdf/ET.pdf"
    else:
        ps = pages(fk); n = norm(needle); page=None
        for i,t in enumerate(ps):
            if n in t: page=i+1; break
        if page is None: miss.append((iid,needle)); page=1
        src = FILES[fk][1]; file=f"pdf/{fk}.pdf"
    items[iid]=dict(src=src, label=label, text=text, page=page, file=file, kind=KIND(fk), recheck=RECHECK.get(iid))
used=set()
for gl in G:
    for iid,_ in gl["items"]:
        assert iid in items, iid; used.add(iid)
print("missing pages:", miss)
print("unused items:", sorted(set(items)-used))
os.makedirs("/home/claude/build/site/pdf", exist_ok=True)
for fk,(base,_) in FILES.items(): shutil.copy(f"{SRC}/{base}.pdf", f"/home/claude/build/site/pdf/{fk}.pdf")
json.dump(dict(items=items, goals=G), open("/home/claude/build/site/data.json","w"), ensure_ascii=False)
print(len(items), "items,", len(G), "goals")
