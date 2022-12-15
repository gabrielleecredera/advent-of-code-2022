import re

inputs = open('input.txt').read().splitlines()
walls = set()
max_y = 0
for input in inputs:
    points = re.findall(r'(\d+),(\d+)', input)
    for i in range(len(points) - 1):
        from_pt = (int(points[i][0]), int(points[i][1]))
        to_pt = (int(points[i + 1][0]), int(points[i + 1][1]))
        if max(from_pt[1], to_pt[1]) > max_y:
            max_y = max(from_pt[1], to_pt[1])
        if from_pt[0] != to_pt[0]:
            for j in range(min(from_pt[0], to_pt[0]), max(from_pt[0], to_pt[0]) + 1):
                walls.add((j, from_pt[1]))
        elif from_pt[1] != to_pt[1]:
            for j in range(min(from_pt[1], to_pt[1]), max(from_pt[1], to_pt[1]) + 1):
                walls.add((from_pt[0], j))

valid_dirs = [
    (0, 1),
    (-1, 1),
    (1, 1),
]

sand_pos = (500, 0)
rest_count = 0
while True:
    if sand_pos[1] > max_y:
        print(rest_count)
        break
    changed_pos = False
    for dir in valid_dirs:
        tentative_pos = (sand_pos[0] + dir[0], sand_pos[1] + dir[1])
        if tentative_pos not in walls:
            sand_pos = tentative_pos
            changed_pos = True
            break
    if not changed_pos:
        rest_count += 1
        walls.add(sand_pos)
        sand_pos = (500, 0)
