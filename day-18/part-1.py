import re
import itertools

cubes = re.findall(r'(-?\d+),(-?\d+),(-?\d+)', open('input.txt').read())
cubes = list(map(lambda cube: tuple(map(int, cube)), cubes))

area = 0
combos = [
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, -1),
]
for cube in cubes:
    for combo in combos:
        if tuple(a + d for a, d in zip(cube, combo)) not in cubes:
            area += 1
print(area)
