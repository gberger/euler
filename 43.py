import itertools

def interesting():
    p = []
    for x in itertools.permutations(['0','1','2','3','4','5','6','7','8','9']):
        s = ''.join(list(x))
        n = int(s)
        if n>=1234567890:
            if int(s[1:4])%2==0 and int(s[2:5])%3==0 and int(s[3:6])%5==0 and int(s[4:7])%7==0 and int(s[5:8])%11==0 and int(s[6:9])%13==0 and int(s[7:10])%17==0:
                p.append(n)
    return p
        
i = interesting()
print i, sum(i)