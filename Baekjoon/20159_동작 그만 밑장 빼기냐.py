import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

res = 0

for i in range(N):
    if i % 2 == 0:
        res += card[i]

origin = res
ans = origin

for i in range(N-1, 0, -2):
    res += card[i]
    res -= card[i-1]
    print(res)
    ans = max(ans, res)

res = origin
for i in range(N-2, 1, -2):
    res -= card[i]
    res += card[i-1]
    print(res)
    ans = max(ans, res)

print(ans)
