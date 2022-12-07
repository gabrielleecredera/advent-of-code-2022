import re
import math
from collections import defaultdict

input = open("input.txt").read().splitlines()
fs = defaultdict(lambda: 0)
current_path = []

for line in input:
    arguments = line.split(' ')
    if arguments[0] == '$':
        if arguments[1] == 'cd':
            if arguments[2] == '..':
                current_path = current_path[:-1]
            elif arguments[2] == '/':
                current_path = ['']
            else:
                current_path.append(arguments[2])
    else:
        if arguments[0] != 'dir':
            for k in range(len(current_path)):
                fs['/'.join(current_path[:k + 1])] += int(arguments[0])

print(sum([size for size in fs.values() if size <= 100_000]))

required_space = 30000000 - (70000000 - fs[''])
print(sorted([size for size in fs.values() if size >= required_space])[0])
