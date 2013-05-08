import copy

#preparing
f = open("18.txt", "r")
contents = f.read()
lines = contents.split('\n')
triangle = [line.split(' ') for line in lines]
l = len(triangle[-1])
for line in triangle:
    for i in range(0,len(line)):
        line[i] = int(line[i])
    line += [0]*(l-len(line))
    
m = copy.deepcopy(triangle)
for i in range(1, l):
    for j in range(0,l):
        curr = m[i][j]
        if curr!=0:
            if j!=0:
                m[i][j] += max([m[i-1][j-1], m[i-1][j]])
            else:
                m[i][j] += m[i-1][j]
            
print max(m[-1])