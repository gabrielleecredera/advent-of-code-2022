import re

pairs = []
for line in open('input.txt').read().splitlines():
    parsed = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
    pairs.append([list(map(int, parsed[0])), list(map(int, parsed[1]))])

min_num = 0
max_num = 4000000

for row in range(0, max_num + 1):
    ranges = []
    counter = 0

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
        new_range = [max(min_num, new_range[0]), min(max_num, new_range[1])]
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
                ranges[i] = [new_range[0], new_range[1]]
                added = True
                break
            if new_range[0] >= range_el[0] and new_range[1] <= range_el[1]:
                added = True
                continue
        if not added:
            ranges.append(new_range)

    for [s, e] in ranges:
        counter += e - s + 1
    if counter < max_num + 1:
        print(row)
        for i in range(len(ranges) - 1):
            if abs(ranges[i][1] - ranges[i + 1][0]) > 0:
                x = sorted([ranges[i], ranges[i + 1]])
                print((x[0][1] + 1) * 4000000 + row)
                exit()
