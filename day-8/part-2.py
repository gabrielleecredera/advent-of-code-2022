import re
import math

input = open("input.txt").read().splitlines()
best_score = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        height = int(input[y][x])
        counters = [0, 0, 0, 0]
        for check_y in range(y - 1, -1, -1):
            counters[0] += 1
            if int(input[check_y][x]) >= height:
                break
        for check_y in range(y + 1, len(input)):
            counters[1] += 1
            if int(input[check_y][x]) >= height:
                break
        for check_x in range(x - 1, -1, -1):
            counters[2] += 1
            if int(input[y][check_x]) >= height:
                break
        for check_x in range(x + 1, len(line)):
            counters[3] += 1
            if int(input[y][check_x]) >= height:
                break
        score = counters[0] * counters[1] * counters[2] * counters[3]
        if score > best_score:
            best_score = score

print(best_score)
