result = 0
for base in range(1,1000):
    for p in range(1,30):
        num = base**p
        if len(str(num)) == p:
            result += 1
        if len(str(num)) > p:
            break
            
            
print result