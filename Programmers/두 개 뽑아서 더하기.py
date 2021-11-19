from itertools import combinations

def solution(numbers):
    answer = set()
    comb = list(combinations(numbers, 2))
    
    for c in comb:
        answer.add(sum(c))
            
    return sorted(list(answer))
