import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0 for i in range(M+1)]
    dp[0] = 1

    for i in coin:
        for j in range(1, M+1):
            if j-i >= 0:
                dp[j] += dp[j-i]

    print(dp[M])