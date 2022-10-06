import sys, math

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

max_value = -math.inf
min_value = math.inf
def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value
    if i == N:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / num[i]))
            div += 1

dfs(1, num[0])

print(max_value)
print(min_value)