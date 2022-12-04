import re
import math

input = open("input.txt").read()
parsed_input = re.findall('(\d+)-(\d+),(\d+)-(\d+)', input)

count = 0
for pair in parsed_input:
    a_start, a_end = [int(pair[0]), int(pair[1])]
    b_start, b_end = [int(pair[2]), int(pair[3])]
    if (a_start <= b_start and a_end >= b_end) or (a_start >= b_start and a_end <= b_end):
        count += 1
print(count)
