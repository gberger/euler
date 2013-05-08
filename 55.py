def process(num):
    return num + int(str(num)[::-1])
    
def ispal(num):
    return num == int(str(num)[::-1])
    
def lycherel(num):
    for i in range(50):
        num = process(num)
        if ispal(num):
            return True
    return False        
     
    
qtty = 0
for i in range(10000):
    if not lycherel(i):
        qtty += 1

print qtty