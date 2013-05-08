arr = [0] * 10000001
arr[1] = 1
arr[89] = 89

def next(n):
    st = str(n)
    sum = 0
    for s in st:
        sum += int(s)**2
    return sum

def genseq(n):
    seq = [n]
    nex = next(n)
    while True:
        seq.append(nex)
        nex = next(nex)
        if nex == 1 or nex == 89:
            break
        if arr[nex] != 0:
            nex = arr[nex]
            break
    for s in seq:
        arr[s] = nex
    return seq
        
for i in range(2,10000001):
    genseq(i)
    