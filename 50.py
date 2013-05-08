from bisect import bisect

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


plist = [n for n in range(50001) if isprime(n)]
pl = len(plist)

longest = 21
s=0
for a in range(pl):
    for b in range(pl):
        if b>a:
            s = sum(plist[a:b+1])
            if s<1000000 and isprime(s) and b-a>longest:
                longest = b-a
                print s, "=>", longest, plist[a:b+1]