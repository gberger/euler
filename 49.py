from itertools import permutations, combinations

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

def hasseq(arr):
    for x in combinations(arr, 3):
        if x[2]-x[1] == x[1]-x[0] and x[2]!=x[1]!=x[0]:
            print x
    return False
    
    
for n in range(1000,10000):
    if isprime(n):
        pper = []
        for x in permutations(str(n)):
            x = int(''.join(x))
            if isprime(x):
                pper.append(x)
        hasseq(pper)