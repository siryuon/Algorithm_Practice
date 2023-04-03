def solution(genres, plays):
    answer = []
    lst = []
    dic = {}

    lst = [[genres[i], plays[i], i] for i in range(len(genres))]
    
    for l in lst:
        if l[0] not in dic:
            dic[l[0]] = l[1]
        else:
            dic[l[0]] += l[1]
    
    lst = sorted(lst, key=lambda x: (x[0], -x[1], x[2]))
    items = sorted(dic.items(), key = lambda x: -x[1])

    for item in items:
        cnt = 0
        for l in lst:
            if item[0] == l[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(l[2])

    return answer