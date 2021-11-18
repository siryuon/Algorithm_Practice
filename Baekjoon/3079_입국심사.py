import sys

N, M = map(int, sys.stdin.readline().split())

judge = []
for _ in range(N):
    judge.append(int(sys.stdin.readline()))
                 
left = min(judge)
result = right = max(judge) * M

while left <= right:
    total = 0
    mid = (left + right) // 2

    for i in range(N):
        total += mid // judge[i]

    if total >= M:
        right = mid -1
        result = min(result, mid)
    else:
        left = mid + 1

print(result)
