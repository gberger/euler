from math import sqrt

def ispen(n):
    s = (sqrt(24*n+1)+1)/6
    return s == int(s)

    
def genpen(n):
    return n*(3*n-1)/2
    
i = 0
pen = [1]
while True:
    i+=1
    pen.append(i*(3*i-1)/2)
    for j in range(2, len(pen)-1):
        if ispen(pen[i]-pen[j]) and ispen(pen[i]+pen[j]):
            print pen[i]-pen[j]
            break