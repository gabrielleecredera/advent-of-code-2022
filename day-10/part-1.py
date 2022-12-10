import re
import math

step = 0
x = 1
counter = 0

input = open("input.txt").read().splitlines()
for index, line in enumerate(input):
    if line == 'noop':
        step += 1
        if step in [20, 60, 100, 140, 180, 220]:
            counter += step * x
            print(step, x)
    else:
        [ins, val] = line.split(' ')
        val = int(val)
        step += 2
        if step in [20, 60, 100, 140, 180, 220]:
            counter += step * x
            print(step, x)
        elif step - 1 in [20, 60, 100, 140, 180, 220]:
            counter += (step - 1) * x
            print(step - 1, x)
        x += val

print(counter)
