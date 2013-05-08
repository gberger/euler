def pali10(num):
    num = str(num)
    if num == num[::-1]:
        return True
    return False
    
def pali2(num):
    num = bin(num)[2:]
    if num == num[::-1]:
        return True
    return False

sum=0
for x in range(1,1000000):
    if pali10(x) and pali2(x):
        sum += x
print sum