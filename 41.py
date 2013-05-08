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

def pandigital(n):
    s = str(n)
    l = len(s)
    for i in range(1,l+1):
        if s.count(str(i)) != 1:
            return False
    return True
    
for x in range(1001, 1000001, 2):
    if pandigital(x) and isprime(x):
        print x