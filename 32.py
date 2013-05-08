def ispan(num):
    s = str(num)
    if len(s)!=9:
        return False
    for a in range(1, 10):
        if str(a) not in s:
            return False
    return True
    
li = []
for a in range(1, 10000):
    if "0" not in st
    for b in range(1, 10000):
        if b>a:
            st = str(a) + str(b) + str(a*b)
            if ispan(st):
                print a, b, a*b
                li.append(a*b)

print set(li)
print sum(set(li))