def solution(a, b):
    answer = 0
    for l, r in zip(a, b):
        answer += l * r
    return answer
