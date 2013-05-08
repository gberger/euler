def factorial(n):
    result = 1
    for i in xrange(1, abs(n)+1):
        result *= i
    if n >= 0:
        return result
    else:
        return -result

def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n-k))

def numcomb(n, k):
    return binomial(n+k-1, k)
    
sum = 0
for l in range(0,101):
    sum += numcomb(10,l) + numcomb(9, l)
    print l, sum-1002
    
