import re
import math

max = 0
current = 0

for line in open("input.txt"):
    if line == '\n':
        if current > max:
            max = current
        current = 0
    else:
        current += int(line)

print(max)