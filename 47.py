import time

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
       
primelist = [2]+[n for n in range(3,1000, 2) if isprime(n)]
time.clock()
def factors(n):
    global primelist
    result = []
    for i in primelist:
        if i > n/2:
            return result  
        if n%i==0:
            result.append(i)
    return result

found = 0
i = 0
while found<4:
    if len(factors(i))==4:
        found += 1
    else:
        found = 0
    i+=1

for n in range(i-4, i):
    print n, factors(n)
print time.clock()