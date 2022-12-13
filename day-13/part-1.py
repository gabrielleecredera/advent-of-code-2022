import re
import math

def compare(left, right):
    in_order = None
    for index in range(min(len(left), len(right))):
        if type(left[index]) == int and type(right[index]) == list:
            left[index] = [left[index]]
        if type(right[index]) == int and type(left[index]) == list:
            right[index] = [right[index]]
        if type(left[index]) == int and type(right[index]) == int:
            if left[index] > right[index]:
                return False
            if left[index] < right[index]:
                return True
        if type(left[index]) == list and type(right[index]) == list:
            result = compare(left[index], right[index])
            if result is not None:
                return result
    if in_order is None:
        if len(left) < len(right):
            return True
        if len(right) < len(left):
            return False
    return in_order

input = open("input.txt").read().split('\n\n')
indexes = []
for pair_index, pair in enumerate(input):
    [left, right] = map(eval, pair.split('\n')[0:2])
    result = compare(left, right)
    if result:
        indexes.append(pair_index + 1)

print(sum(indexes))
