def isbouncy(n):
    s = str(n)
    if len(s)<3:
        return 0
    if ''.join(sorted(s)) == s:
        return 0
    if ''.join(sorted(s)[::-1]) == s:
        return 0
    return 1
    
ratio = 0
bouncies = 0
l = 0
i = 0
while ratio!=0.99:
    i+=1
    l += 1
    bouncies += isbouncy(i)
    ratio = float(bouncies)/l
    if i%10000==0:
        print i, ratio
print i, ratio