import itertools

def pad(n):
    divisors = [i for i in range(1, n/2+1) if n%i==0]
    s = sum(divisors)
    if s == n:
        return 0
    elif s>n:
        return 1
    else:
        return -1
    
abun = []
for i in range(1,14200):
    padi = pad(i)
    if padi == 1:
        abun.append(i)
    
li = []
for x in itertools.combinations_with_replacement(abun, 2):
    li.append(sum(x))
    
li = list(set(li))
print li
cannot = [i for i in range(1,28124) if i not in li]
print cannot
print sum(cannot)