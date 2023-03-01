from collections import defaultdict


def solution(survey, choices):
    answer = ''
    types = [('R','T'),('C','F'),('J','M'),('A','N')]
    scores = defaultdict(int)
    
    for s, c in zip(survey, choices):
        score = abs(c - 4)
        if c < 4:
            scores[s[0]] += score
        else:
            scores[s[1]] += score
            
    for a, b in types:
        if scores[a] >= scores[b]:
            answer = answer + a
        else:
            answer = answer + b

    return answer