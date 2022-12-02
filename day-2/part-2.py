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
score_map = {
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
outcome_scores = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

for round in parsed_input:
    outcome_score = outcome_scores[round[1]]
    total_score += outcome_score
    total_score += shape_scores[[k for k, v in score_map[round[0]].items() if v == outcome_score][0]]

print(total_score)
