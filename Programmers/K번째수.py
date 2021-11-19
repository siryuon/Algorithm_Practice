def solution(array, commands):
    ans = []

    for c in commands:
        spliter = array[c[0]-1:c[1]]
        spliter = sorted(spliter)
        ans.append(spliter[c[2]-1])

    return ans


array = [1,5,2,6,3,7,4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
