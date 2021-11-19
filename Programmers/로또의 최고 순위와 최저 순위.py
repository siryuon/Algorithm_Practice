def solution(lottos, win_nums):
    correct = 0
    
    for l in lottos:
        if l in win_nums:
            correct += 1
            
    min_correct = correct
    max_correct = correct + lottos.count(0)
    
    max_rank = 7 - max_correct
    min_rank = 7 - min_correct

    if max_rank > 5:
        max_rank = 6
    if min_rank > 5:
        min_rank = 6

    return [max_rank, min_rank]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))
