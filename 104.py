def ispan(st):
    s = sorted(st)
    if ''.join(s) == '123456789':
        return True
    return False
    
fibarray = [1, 1, 1]
def genfib(max):
    global fibarray
    l = len(fibarray)
    for n in range(l, max+1):
        fibarray.append(fibarray[n-1] + fibarray[n-2])
            

step = 2500
min = 2500
max = 5000
genfib(max)
found = False
while not found:
    for i in range(min, max):
        n = fibarray[i]
        s1 = str(n%1000000000)
        if not ispan(s1):
            continue
        if not ispan(s2):
            continue
        print "Found! ", i, s1, s2
        found = True
        break
    print "Not found in range %d-%d. Trying %d-%d." % (min, max, min+step, max+step)
    min += step
    max += step
    genfib(max)