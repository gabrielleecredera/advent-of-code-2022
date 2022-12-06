import re
import math

input = open("input.txt").read().splitlines()[0]
for i in range(14, len(input)):
    unique = True
    for index_a, char_a in enumerate(input[i - 14:i]):
        for index_b, char_b in enumerate(input[i - 14:i]):
            if index_a != index_b and char_a == char_b:
                unique = False
                break
        if not unique:
            break
    if unique:
        print(i)
        break
