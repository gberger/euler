from itertools import product

numsp = [1, 2, 3, 4]
pdict = {}
for x in product(numsp, repeat=9):
    s = sum(x)
    if pdict.has_key(s):
        pdict[s] += 1
    else:
        pdict[s] = 1
    
numsc = [1, 2, 3, 4, 5, 6]
cdict = {}       
for x in product(numsc, repeat=6):
    s = sum(x)
    if cdict.has_key(s):
        cdict[s] += 1
    else:
        cdict[s] = 1
    
possibs = 0
beats = 0
for kp, vp in pdict.items():
    for kc, vc in cdict.items():
        if kp>kc:
            beats += vp*vc
        possibs += vp*vc
        
print float(beats)/possibs