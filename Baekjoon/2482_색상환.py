import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

def color(N, K, ans):
    if(N/K == 2):
        return 2
    if(K == 1):
        return N
    
    if(ans[N][K] == 0):
        total = color(N-1, K, ans) + color(N-2, K-1, ans)
        ans[N][K] = total
        return total
    else:
        return ans[N][K]

ans = [[0]*(N+1) for i in range(N+1)]

if N/2 < K:
    print(0)
else:
    print(color(N, K, ans) % 1000000003)
