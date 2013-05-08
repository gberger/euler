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
    
rat = 1
n = 1
diagsize = 1
diagprimes = 0
while rat>0.1:
    n+=2
    diagsize += 4
    diff = n-1
    aaa = [n**2-diff, n**2-2*diff, n**2-3*diff]
    for a in aaa:
            if isprime(a):
                diagprimes += 1
    rat = float(diagprimes)/float(diagsize)
    
print n