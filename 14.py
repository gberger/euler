def sequence_length(starting):
    i=0
    n=starting 
    while n>1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        i += 1
    return i;
    
longest = 0
for i in range(1000000):
    chain = sequence_length(i)
    if(chain>longest):
        longest = chain
        num = i
        print i, chain