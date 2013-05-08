def dlt(n):
    s = str(n)
    for n in s:
        if n not in ['0', '1', '2']:
            return False
    return True

def f(n):
    s = n
    while True:
        if dlt(s):
            return s
        s += n
    
def s(n):
    sum = 0
    for i in range(1, n+1):
        sum += f(i)/i
    return sum

print s(10000)