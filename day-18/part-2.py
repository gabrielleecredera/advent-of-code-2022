import re
import itertools

cubes = re.findall(r'(-?\d+),(-?\d+),(-?\d+)', open('input.txt').read())
cubes = list(map(lambda cube: tuple(map(int, cube)), cubes))
open_waters = set()
area = 0
combos = [
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, -1),
]

# i'm probably over complicating things xd
new_waters = {(-1, -1, -1)}
while new_waters:
    open_waters.update(new_waters)
    new_waters = set()
    for x in range(-1, 21):
        for y in range(-1, 21):
            for z in range(-1, 21):
                pos = (x, y, z)
                if pos in cubes or pos in open_waters:
                    continue
                for combo in combos:
                    if tuple(a + d for a, d in zip(pos, combo)) in open_waters:
                        new_waters.add(pos)
                        break

for cube in cubes:
    for combo in combos:
        if tuple(a + d for a, d in zip(cube, combo)) in open_waters:
            area += 1
print(area)
