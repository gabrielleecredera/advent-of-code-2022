import re

pairs = []
for line in open('input.txt').read().splitlines():
    parsed = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
    pairs.append([list(map(int, parsed[0])), list(map(int, parsed[1]))])

row = 2000000
ranges = []

for pair in pairs:
    s, b = pair
    sb_dist = abs(b[0] - s[0]) + abs(b[1] - s[1])
    target_dist = abs(s[1] - row)
    if sb_dist < target_dist:
        continue
    rel_dist = sb_dist - target_dist
    new_range = [s[0] - rel_dist, s[0] + rel_dist]
    ranges.append(new_range)

for j in range(len(ranges)):
    new_range = ranges.pop(0)
    added = False
    for i, range_el in enumerate(ranges):
        if range_el[0] <= new_range[0] <= range_el[1] and new_range[1] > range_el[1]:
            ranges[i] = [range_el[0], new_range[1]]
            added = True
            break
        if range_el[0] <= new_range[1] <= range_el[1] and new_range[0] < range_el[0]:
            ranges[i] = [new_range[0], range_el[1]]
            added = True
            break
        if new_range[0] < range_el[0] and new_range[1] > range_el[1]:
            ranges[i] = new_range
            added = True
            break
        if new_range[0] >= range_el[0] and new_range[1] <= range_el[1]:
            added = True
            continue
    if not added:
        ranges.append(new_range)

counter = 0
for [s, e] in ranges:
    counter += e - s
print(counter)
