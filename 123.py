def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
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
  
def pe123(n):
    global primelist
    i = n-1
    return ((primelist[i]+1)**n + (primelist[i]-1)**n) % (primelist[i]**2)
    

primelist = [2]+ [a for a in range(3,10000001,2) if isprime(a)]
for i in range(len(primelist)):
    n = i+1
    if pe123(n)>10**10:
        print n, primelist[i], pe123(n)
        break