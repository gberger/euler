from math import sqrt, floor

def pal(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

top = 10**8
itop = int(floor(sqrt(top)))

li = []
    
for i in range(1, itop):
    num = i**2
    for j in range(i+1, itop+1):
        num += j**2
        
        if num>top:
            break
        
        if pal(num):
            li.append(num)
            
print sum(set(li))