import re
import math

total = 0
for line in open("input.txt").read().splitlines():
    compartment_1 = line[:int(len(line) / 2)]
    compartment_2 = line[int(len(line) / 2):]
    common_char = False
    for char_1 in compartment_1:
        for char_2 in compartment_2:
            if char_1 == char_2:
                common_char = char_1
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
