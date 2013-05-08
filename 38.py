def ispan(num):
    s = str(num)
    if len(s)!=9:
        return False
    for a in range(1, 10):
        if str(a) not in s:
            return False
    return True

li = []
    
for a in range(1,10000):
    conc = ''
    n = 1
    while len(conc)<9:
        prod = a*n
        conc += str(prod)
        if ispan(int(conc)):
            li.append(conc)
            print a, n, conc
        n+=1
print max(li)