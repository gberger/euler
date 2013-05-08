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

def nextodd(n):
    if n%2==0:
        return n+1
    else:
        return n+2
    
def nextprime(n):
    n = nextodd(n)
    while True:
        if isprime(n):
            return n
        n+=1

print nextprime(10**14)