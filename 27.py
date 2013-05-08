A = range(-1000,1001)
B = range(-1000,1001)

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

def qqtyprimes(a, b):
    formula = lambda x: x**2 + a*x + b
    foundprime = True
    n=0
    while foundprime:
        foundprime = isprime(formula(n))
        if foundprime:
            n += 1
    return n

maxp = 0

for b in B:
    if isprime(b):
        for a in A:
            p = qqtyprimes(a, b)
            if p > maxp:
                maxp = p
                maxa = a
                maxb = b
                
print maxp, maxa, maxb