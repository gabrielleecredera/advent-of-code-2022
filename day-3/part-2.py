import re
import math

total = 0
input = open("input.txt").read()
parsed_input = re.findall('(\w+)\n(\w+)\n(\w+)', input)
for group in parsed_input:
    common_char = False
    for char_1 in group[0]:
        for char_2 in group[1]:
            for char_3 in group[2]:
                if char_1 == char_2 and char_2 == char_3:
                    common_char = char_1
                    break
            if common_char:
                break
        if common_char:
            break
    prior = ord(common_char)
    if prior > 90:
        prior -= 96
    else:
        prior -= 38
    total += prior
print(total)
