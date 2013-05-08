import time
def wordval(word):
    values = [ord(l)-64 for l in word]
    return sum(values)

def triangleseq(upto):
    return [n*(n+1)/2 for n in range(upto)]
time.clock()
t = triangleseq(30)    
f = open("42.txt", "r")
words = eval('['+f.read()+']')
howmany = 0
for w in words:
    if wordval(w) in t:
        howmany += 1
print howmany
print time.clock()