import re
import math

map = [[j for j in i] for i in open("input.txt").read().splitlines()]

start_pos = (0, 0)
end_pos = (0, 0)
for y_index, row in enumerate(map):
    for x_index, char in enumerate(row):
        if char == 'S':
            start_pos = (x_index, y_index)
        elif char == 'E':
            end_pos = (x_index, y_index)
        else:
            map[y_index][x_index] = ord(map[y_index][x_index]) - 97
queue = [(start_pos, 0)]
min_length = 999999
poses = []

while len(queue):
    pos, length = queue.pop(0)
    if pos == end_pos:
        if length < min_length:
            min_length = length
        continue
    if pos in poses:
        continue
    poses.append(pos)
    height = map[pos[1]][pos[0]]
    if height == 'S':
        height = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos[0] < 0 or new_pos[0] >= len(map[0]) or new_pos[1] < 0 or new_pos[1] >= len(map):
            continue
        new_height = map[new_pos[1]][new_pos[0]]
        if new_height == 'S':
            new_height = 0
        if new_height == 'E':
            new_height = 25
        if new_height > height + 1:
            continue
        queue.append((new_pos, length + 1))

print(min_length)
