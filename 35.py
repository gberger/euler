from itertools import cycle
from math import factorial

def isprime(n):
    '''check if integer n is a prime'''
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True 
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
def cyclelist(num):
    num = list(str(num))
    li = []
    
    for i in range(len(num)):
        li.append(int(''.join(num)))
        num.append(num.pop(0))
    return li
    
def checkd(num):
    if int(num)<10:
        return True
    num = list(str(num))
    for i in num:
        if int(i)%2==0:
            return False
    return True
    
qtty = 0
circp = []
for num in range(2,1000000):
    if checkd(num):
        if isprime(num):
            li = cyclelist(num)
            li2 = [n for n in li if isprime(n)]
            if li == li2:
                circp.append(num)
                print num
print len(circp)
        