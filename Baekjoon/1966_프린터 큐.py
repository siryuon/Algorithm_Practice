import sys


t = int(sys.stdin.readline())

for _ in range(t):
    N, M = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    target = lst[M]
    cnt = 0
    location = M
    
    while lst:
        high = max(lst)
        if lst[0] < high:
            if location == 0:
                low = lst.pop(0)
                lst.append(low)
                location = len(lst) - 1
            else:
                low = lst.pop(0)
                lst.append(low)
                location -= 1
                
        else:
            done = lst.pop(0)
            cnt += 1
            if done == target and location == 0:
                print(cnt)
                break
            else:
                location -= 1
