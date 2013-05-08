from itertools import permutations
li=[]
for x in permutations("123456789"):
    s = ''.join(x)
    for a in range(1,5):
        for b in range(1, 5):
            if b+a<8:
                num1 = s[:a]
                num2 = s[a:(b+a)]
                num3 = s[(b+a):]
                if int(num1)*int(num2) == int(num3):
                    print num1, num2, num3
                    li.append(int(num3))
                    
                    
print set(li)
print sum(set(li))