import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = dict()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
    
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

visited=[1]
linked = graph[1]

while linked:
    l = linked.pop()
    if l not in visited:
        visited.append(l)
        linked.extend(graph[l])
        
print(len(visited)-1)   
