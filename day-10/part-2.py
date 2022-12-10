import re
import math

step = 0
x = 1


def print_new(step):
    if x == step % 40 or x + 1 == step % 40 or x - 1 == step % 40:
        print('##', end='')
    else:
        print('  ', end='')
    if (step + 1) % 40 == 0:
        print()


input = open("input.txt").read().splitlines()
for index, line in enumerate(input):
    if line == 'noop':
        print_new(step)
        step += 1
    else:
        [ins, val] = line.split(' ')
        val = int(val)
        print_new(step)
        step += 1
        print_new(step)
        step += 1
        x += val
