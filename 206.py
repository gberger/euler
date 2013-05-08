from math import sqrt
import re

max = 19293949596979899
n = int(sqrt(max))+1

while not re.match("1\d2\d3\d4\d5\d6\d7\d8\d9", str(n*n)):
    n -= 2

print n