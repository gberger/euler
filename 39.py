from math import sqrt
most = 0
pp =0
squares = [i*i for i in range(0,1001)]
possibs = [0]*1001
for a in range(1,1001):
    for b in range(1, a):
        c = sqrt(squares[a]+squares[b])
        if int(c) == c:
            c = int(c)
            p = a+b+c
            if p<1000:
                possibs[p]+=1
                
print max(possibs), possibs.index(max(possibs))