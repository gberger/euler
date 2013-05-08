f = open("22.txt", "r")
list = eval('[' + f.read() + ']')
list.sort()


sum = 0
for i in range(len(list)):
    posscore = i+1
    letterscore = 0
    for letter in list[i]:
        letterscore += ord(letter)-64
    score = posscore * letterscore
    sum += score
    
print sum