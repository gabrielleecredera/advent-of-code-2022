import re
import math

all_count = []
current = 0

for line in open("input.txt"):
    if line == '\n':
        all_count.append(current)
        current = 0
    else:
        current += int(line)

print(sum(sorted(all_count)[-3:]))