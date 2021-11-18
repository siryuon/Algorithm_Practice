import sys

N, M, V = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(N+1)]

for n in range(M):
    x, y = map(int, sys.stdin.readline().split())
    edge[x].append(y)
    edge[y].append(x)

for e in edge:
    e.sort(reverse=True)

def dfs():
    visited=[]
    stack=[V]
    flag=[0 for _ in range(N+1)]

    while stack:
        v = stack.pop()
        if not flag[v]:
            flag[v] = 1
            visited.append(str(v))
            stack.extend(edge[v])
            
    return " ".join(visited)

def bfs():
    visited = []
    queue = [V]
    flag = [0 for _ in range(N+1)]
    flag[V] = 1

    while queue:
        v = queue.pop()
        visited.append(str(v))
        for i in reversed(edge[v]):
            if not flag[i]:
                flag[i] = 1
                queue = [i] + queue
                
    return " ".join(visited)

print(dfs())
print(bfs())
