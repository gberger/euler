def checkio(number):
    known = {0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five", 
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten", 
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred",
            1000: "thousand",
    }
    if number==0:
        return known[0]
        
    centenas = int(number/100)
    dezenas = int((number%100)/10)
    unidade = int(number%10)
    string = ""
    if centenas>0:
        string += "%d %s" % (centenas, known[100])
    if dezenas>1:
        string += "%s " % (known[10*dezenas])
        if unidade>1:
            string += "%s" % (known[unidade])
    elif dezenas==1:
        string += "%s " % (known[10*dezenas+unidade])
    else:
        string += "%s" % (known[unidade])
    return string

if __name__ == '__main__':
    for i in range(1,1001):
        print i,checkio(i)