def d(n):
    divisors = [i for i in range(1, n/2+1) if n%i==0]
    return sum(divisors)
    
listtups = [(i, d(i)) for i in range(1,10001)]
dict = {k: v for (k, v) in listtups}

def amicable_sum(dict):
    sum=0
    for i in range(1,10001):
        for j in range(2,10001):
            if j>i and dict[i]==j and dict[j]==i:
                sum += j+i
    return sum
    
print amicable_sum(dict)