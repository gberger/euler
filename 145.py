def isrev(num1):
    s1 = str(num1)
    if s1[-1] == '0':
        return False
    s2 = s1[::-1]
    num2 = int(s2)
    num3 = num1+num2
    s3 = str(num3)
    for n in s3:
        if int(n)%2==0:
            return False
    return True
    
num = 0
for i in xrange(1, 10**9):
    if isrev(i):
        num += 1
    if i%10**6==0:
        print i
print num