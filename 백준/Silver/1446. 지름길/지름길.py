import sys

input = sys.stdin.readline
n, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [i for i in range(d+1)]

for i in range(d+1):
    dist[i] = min(dist[i], dist[i-1]+1)
    for s, e, shortcut in graph:
        if i == s and e <= d and dist[i] + shortcut < dist[e]:
            dist[e] = dist[i] + shortcut

print(dist[d])