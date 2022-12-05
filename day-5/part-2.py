import re
import math

input = open("input.txt").read()
[starting_pos, instructions] = input.split('\n\n')
starting_pos = starting_pos.splitlines()

stacks = []
for i in range(int(starting_pos[-1][-1])):
    stacks.append([])
starting_pos = starting_pos[:-1]

for line in starting_pos:
    for i in range(len(stacks)):
        if i * 4 + 1 > len(line):
            break
        if line[i * 4 + 1] != ' ':
            stacks[i].insert(0, line[i * 4 + 1])

instructions = re.findall(r'move (\d+) from (\d+) to (\d+)', instructions)
for instruction in instructions:
    top = stacks[int(instruction[1]) - 1][-int(instruction[0]):]
    stacks[int(instruction[1]) - 1] = stacks[int(instruction[1]) - 1][:-int(instruction[0])]
    stacks[int(instruction[2]) - 1].extend(top)

for stack in stacks:
    print(stack[-1], end='')
