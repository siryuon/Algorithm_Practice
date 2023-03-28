import sys, math
from itertools import combinations
from collections import deque, defaultdict

input = sys.stdin.readline

def bfs(comb):
    start = comb[0]
    queue = deque([start])
    visited = set([start])
    _sum = 0
    while queue:
        v = queue.popleft()
        _sum += pp[v]
        for u in g[v]:
            if u not in visited and u in comb:
                queue.append(u)
                visited.add(u)
    return _sum, len(visited)

n = int(sys.stdin.readline().strip())
pp = [int(x) for x in input().split()]
g = defaultdict(list)
result = math.inf

for i in range(n):
    _input = [int(x) for x in input().split()]
    for j in range(1, _input[0]+1):
        g[i].append(_input[j] - 1)

for i in range(1, n // 2 + 1):
    combs = list(combinations(range(n), i))
    for comb in combs:
        sum1, v1 = bfs(comb)
        sum2, v2 = bfs([i for i in range(n) if i not in comb])
        if v1 + v2 == n:
            result = min(result, abs(sum1 - sum2))

if result != math.inf:
    print(result)
else:
    print(-1)
