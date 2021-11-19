def solution(participant, completion):
    answer = {}
    
    for p in participant:
        if p not in answer:
            answer[p] = 1
        else:
            answer[p] += 1
    for c in completion:
        answer[c] -= 1
        
    answer = {v:k for k,v in answer.items()}

    return answer.get(1)
