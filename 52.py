def ispal(a, b):
    la = sorted(str(a))
    lb = sorted(str(b))
    return la==lb
    
i=1
while True:
    i+=1
    if ispal(i, i*2) and ispal(i, i*3) and ispal(i, i*4) and ispal(i,i*5) and ispal(i, i*6): 
        break
        
print i