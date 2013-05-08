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

oddcomp = [i for i in range(35,10001,2) if not isprime(i)]
prime = [2] + [i for i in range(3, 10001, 2) if isprime(i)]
tsq = [2*(i**2) for i in range(1,100)]

def issum(num):
    global prime, tsq
    for i in prime:
        for j in tsq:
            if i+j == num:
                return True
    return False

for i in oddcomp:
    if not issum(i):
        print i