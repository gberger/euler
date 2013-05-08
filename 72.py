def isred(n, d):
    if d%n==0:
        return False
    return True

qtty = 0
for d in range(1000001):
    for n in range(1,d,2):
        if isred(n, d):
            qtty += 1

    if d%10000==0:
        print d
print qtty