import re
import math

input = open("input.txt").read().splitlines()
counter = 0
for y, line in enumerate(input):
    if y == 0 or y == len(input) - 1:
        counter += len(input[0])
        continue
    for x, char in enumerate(line):
        if x == 0 or x == len(line) - 1:
            counter += 1
            continue
        height = int(input[y][x])
        visible = True
        for check_y in range(0, y):
            if int(input[check_y][x]) >= height:
                visible = False
                break
        if visible:
            counter += 1
            continue
        visible = True
        for check_y in range(y + 1, len(input)):
            if int(input[check_y][x]) >= height:
                visible = False
                break
        if visible:
            counter += 1
            continue
        visible = True
        for check_x in range(0, x):
            if int(input[y][check_x]) >= height:
                visible = False
                break
        if visible:
            counter += 1
            continue
        visible = True
        for check_x in range(x + 1, len(line)):
            if int(input[y][check_x]) >= height:
                visible = False
                break
        if visible:
            counter += 1
            continue

print(counter)
