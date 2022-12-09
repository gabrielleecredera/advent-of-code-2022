import re
import math

steps = re.findall(r'(\w) (\d+)', open("input.txt").read())

head_pos = [0, 0]
tail_pos = [0, 0]
tail_pos_list = set()
dirs = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0],
}
for step in steps:
    for i in range(int(step[1])):
        head_pos[0] += dirs[step[0]][0]
        head_pos[1] += dirs[step[0]][1]

        if head_pos[0] == tail_pos[0] and abs(head_pos[1] - tail_pos[1]) == 2:
            tail_pos[1] += 1 if head_pos[1] > tail_pos[1] else -1
        elif head_pos[1] == tail_pos[1] and abs(head_pos[0] - tail_pos[0]) == 2:
            tail_pos[0] += 1 if head_pos[0] > tail_pos[0] else -1
        elif abs(head_pos[0] - tail_pos[0]) + abs(head_pos[1] - tail_pos[1]) >= 3:
            tail_pos[0] += 1 if head_pos[0] > tail_pos[0] else -1
            tail_pos[1] += 1 if head_pos[1] > tail_pos[1] else -1
        tail_pos_list.add((tail_pos[0], tail_pos[1]))

print(len(tail_pos_list))
