target = 100
ways = [0]*101
ways[0] = 1
for i in range(1,101):
    for j in range(i, target+1):
        ways[j] += ways[j-i]
    print i, ways[i]    
