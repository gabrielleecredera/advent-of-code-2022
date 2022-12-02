import re
import math

input = open("input.txt").read()
parsed_input = re.findall('([ABC]) ([XYZ])', input)
total_score = 0

shape_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}
outcome_scores = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3,
    },
}

for round in parsed_input:
    total_score += shape_scores[round[1]] + outcome_scores[round[0]][round[1]]

print(total_score)
