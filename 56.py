max = 1
for a in range(100):
    for b in range(100):
        n = a**b
        s = str(n)
        sum = 0
        for l in s:
            sum += int(l)
        if sum>max:
            max = sum
            
print max