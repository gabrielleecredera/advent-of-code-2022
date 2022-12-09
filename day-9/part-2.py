import re
import math

steps = re.findall(r'(\w) (\d+)', open("input.txt").read())

all_pos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
tail_pos_list = set()
dirs = {
    'U': [0, -1],
    'D': [0, 1],
    'L': [-1, 0],
    'R': [1, 0],
}
for step in steps:
    for i in range(int(step[1])):
        head_pos = all_pos[0]
        all_pos[0][0] += dirs[step[0]][0]
        all_pos[0][1] += dirs[step[0]][1]
        for j in range(1, 10):
            prev_pos = all_pos[j - 1]
            pos = all_pos[j]
            if prev_pos[0] == pos[0] and abs(prev_pos[1] - pos[1]) == 2:
                all_pos[j][1] += 1 if prev_pos[1] > pos[1] else -1
            elif prev_pos[1] == pos[1] and abs(prev_pos[0] - pos[0]) == 2:
                all_pos[j][0] += 1 if prev_pos[0] > pos[0] else -1
            elif abs(prev_pos[0] - pos[0]) + abs(prev_pos[1] - pos[1]) >= 3:
                all_pos[j][0] += 1 if prev_pos[0] > all_pos[j][0] else -1
                all_pos[j][1] += 1 if prev_pos[1] > all_pos[j][1] else -1
        tail_pos_list.add((all_pos[-1][0], all_pos[-1][1]))

print(len(tail_pos_list))
