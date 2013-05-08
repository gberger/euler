def sumspiral(n):
    if n%2 == 0:
        return
    if n == 1:
        return 1
    
    sum = 1
    for b in range(3, n+1, 2):
        sq = b**2
        diff = b-1
        sum += 4*sq - 6*diff
    return sum
    
print sumspiral(9999999)
