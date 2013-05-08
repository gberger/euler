from math import sqrt

def ispen(n):
    p = (sqrt(1+24*n)+1)/6
    return p == int(p)
    
def hex(n):
    return n*(2*n-1)
    
n = 144
while not ispen(hex(n)):
    n+=1
    
print hex(n)


