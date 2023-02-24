s = list(input())
t = list(input())
flag = False

def dfs(t):
    global flag
    if t == s:
        flag = True

    if len(t) == 0:
        return 0

    if t[-1] == 'A':
        dfs(t[:-1])

    if t[0] == 'B':
        t = t[1:]
        dfs(t[::-1])

dfs(t)
if flag:
    print(1)
else:
    print(0)