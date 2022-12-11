import re
import math

input = open("input.txt").read().split('\n\n')
monkey_inputs = {}
monkeys = []
counter = []

for monkey in input:
    lines = monkey.splitlines()
    monkeys.append({
        'starting_items': list(map(int, lines[1].split(': ')[1].split(', '))),
        'operation': lines[2].split('old ')[1][0],
        'operation_target': lines[2].split(' ')[-1],
        'test': int(lines[3].split('divisible by ')[1]),
        'true': int(lines[4][-1]),
        'false': int(lines[5][-1])
    })
    counter.append(0)

for i in range(20):
    for monkey_i, monkey in enumerate(monkeys):
        while len(monkey['starting_items']):
            item = monkey['starting_items'].pop(0)
            counter[monkey_i] += 1
            operation_target = monkey['operation_target']
            if operation_target == 'old':
                operation_target = item
            else:
                operation_target = int(operation_target)
            if monkey['operation'] == '+':
                new = item + operation_target
            else:
                new = item * operation_target
            new = int(new / 3)
            if new % monkey['test'] == 0:
                monkeys[monkey['true']]['starting_items'].append(new)
            else:
                monkeys[monkey['false']]['starting_items'].append(new)

print(sorted(counter)[-2] * sorted(counter)[-1])