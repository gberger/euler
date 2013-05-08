from math import factorial

def C(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

l = []
for n in range(23, 101):
    for r in range(1, n):
        if C(n,r)>1000000:
            l.append('oi')
            
print len(l)