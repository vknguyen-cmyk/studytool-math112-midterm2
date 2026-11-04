import json, sys, os, shutil, re
sys.path.insert(0, "/home/claude/build")
from items import L
from goals import G
from typed import T
from crop import FILES, SRC

SRCNAME = {"L9":"Lecture 9","L10":"Lecture 10","L11":"Lecture 11","L12":"Lecture 12","L13":"Lecture 13","L14":"Lecture 14","L15":"Lecture 15","L16":"Lecture 16",
 "HW5":"Homework 5","HW6":"Homework 6","HW7":"Homework 7","HW8":"Homework 8","HW9":"Homework 9","PA":"Practice Exam 2A","PB":"Practice Exam 2B"}
kind = lambda fk: "lecture" if fk.startswith("L") else "homework" if fk.startswith("HW") else "exam"
meta = json.load(open("/home/claude/build/cropmeta.json"))
items = {}
for iid,(fk,label,needle,text) in L.items():
    if iid in meta:
        m = meta[iid]
        lab = re.sub(r"^§\d+(\.\d+)?\s*", "", label) if fk.startswith("L") else label
        sec = (re.match(r"^(§\d+(\.\d+)?)", label) or [None])[0] if fk.startswith("L") else None
        items[iid] = dict(kind=kind(fk), src=SRCNAME[fk], label=lab, sec=sec, img=f"img/{iid}.png", w=m["w"], h=m["h"],
                          page=m["page"], pdf=f"pdf/{fk}.pdf", search=m["txt"][:600])
for iid,src,label,prompt,choices,style in T:
    items[iid] = dict(kind="ticket" if iid.startswith("ET") else "pcrq", src=src, label=label, prompt=prompt, choices=choices, style=style,
                      search=prompt+" "+" ".join(choices or []))

EXTRA = {2:["L9.D22","L9.D23"],4:["L10.P21"],6:["L9.T24"],20:["L13.T11"],28:["L13.D21","L13.D31"],29:["L13.D31"],
         30:["L13.E21"],35:["L14.E21"],37:["L14.D21"],41:["L14.E31"]}
goals=[]
for g in G:
    its=[]
    for iid,note in g["items"]:
        if iid not in items: continue          # personal reflection questions dropped
        note = "" if re.search(r"missed|recheck", note) else note
        note = re.sub(r"^partial:?\s*", "", note) if note.startswith("partial") else note
        its.append([iid, note])
    for iid in EXTRA.get(g["n"], []):
        if iid not in [i for i,_ in its]: its.append([iid,""])
    order = {"lecture":0,"homework":1,"pcrq":2,"ticket":3,"exam":4}
    its.sort(key=lambda x: order[items[x[0]]["kind"]])
    goals.append(dict(n=g["n"], week=g["week"], text=g["text"], star=g["star"], items=its))
used = {i for g in goals for i,_ in g["items"]}
items = {k:v for k,v in items.items() if k in used}
out="/home/claude/build/site2"
os.makedirs(out+"/pdf", exist_ok=True)
for fk,base in FILES.items(): shutil.copy(f"{SRC}/{base}.pdf", f"{out}/pdf/{fk}.pdf")
for f in os.listdir(out+"/img"):
    if f[:-4] not in used: os.remove(f"{out}/img/{f}")
json.dump(dict(items=items, goals=goals), open(out+"/data.json","w"), ensure_ascii=False)
print(len(items),"items", len(goals),"goals", sum(1 for v in items.values() if "img" in v),"crops")
