def solution(progresses, speeds):
    answer = []
    end = 0 
    while sum(answer) != len(progresses):
        finish = 0

        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        print(progresses)
        if progresses[end] < 100:
            continue
        else:
            for p in progresses[end:]:
                print(p)
                if p >= 100:
                    finish += 1
                else:
                    break
            end += finish
            answer.append(finish)

        print('ans: ', answer)
    return answer


progresses = [95,90,99,99,80,99]
speeds=[1,1,1,1,1,1]

print(solution(progresses, speeds))
