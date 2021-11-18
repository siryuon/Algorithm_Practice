import sys

n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    c = int(sys.stdin.readline())
    coins.append(c)

coins = sorted(coins, reverse=True)

pay = 0
cnt=[0 for _ in range(len(coins))]

for i in range(len(coins)):
    if pay == 0:
        num = k // coins[i]
    else:
        num = (k - pay) // coins[i]
    pay = pay + num * coins[i]
    cnt[i] += num
    if pay == k:
        break

print(sum(cnt))
