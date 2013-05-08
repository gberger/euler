from math import factorial
for number in range(3,9999999):
    sum = 0
    for digit in str(number):
        sum += factorial(int(digit))
    if sum == number:
        print number