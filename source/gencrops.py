import os, sys, json
sys.path.insert(0,'/home/claude/build')
from items import L
from cropspec import spec
import crop
os.makedirs('/home/claude/build/site2/img', exist_ok=True)
meta={}; errs=[]
for iid,(fk,label,needle,text) in L.items():
    if fk in ('ET',) or fk.startswith('P') and fk[1:].isdigit(): continue
    sp = spec(iid)
    try:
        if isinstance(sp, list): im,page,txt = crop.crop_multi(fk, sp, f'/home/claude/build/site2/img/{iid}.png')
        else:
            st,end,lvl = sp; im,page,txt = crop.crop(fk, st, end, lvl, out=f'/home/claude/build/site2/img/{iid}.png')
        meta[iid]=dict(page=page,w=im.width,h=im.height,txt=txt)
    except Exception as ex: errs.append((iid,str(ex)))
json.dump(meta,open('/home/claude/build/cropmeta.json','w'))
print(len(meta),'crops'); print('errors',errs)
big=sorted(meta.items(),key=lambda kv:-kv[1]['h'])[:12]
for k,v in big: print(k, v['h'], v['page'])
small=sorted(meta.items(),key=lambda kv:kv[1]['h'])[:10]
for k,v in small: print('small',k, v['h'], v['txt'][:60])
