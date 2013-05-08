words = open("words.txt", "r").read().split('\n')
f = open("59.txt", "r")
cont = f.read().split(',')
cont = [int(c) for c in cont]
l = len(cont)
r = range(97,123)

for a in r:
    for b in r:
        for c in r:
            m = ''
            for ch in range(0, l, 3):
                m += (chr(cont[ch]^a)+chr(cont[ch]+1^b)+chr(cont[ch]+2^c))
            if ' ' in m:
                m = m.split(' ')
                for w in m:
                    if w in words:
                        print w, a, b, c
                        print m