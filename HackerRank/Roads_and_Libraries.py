from collections import defaultdict

def dfs(nodes, node, visited):
    if visited[node]:
        return 0
    visited[node] = 1
    cnt = 1
    for neighbor in nodes[node]:
        cnt += dfs(nodes,neighbor, visited)

    return cnt

def roadsAndLibraries(n, c_lib, c_road, cities):
    nodes = {i+1: [] for i in range(n)}
    visited = [0] * (n+1)
    
    for u, v in cities:
        nodes[u].append(v)
        nodes[v].append(u)
        
    cost = 0
    for node in nodes:
        print(node)
        cnt = dfs(nodes, node, visited)
        if cnt:
            cost += c_lib + (cnt-1) * min(c_lib, c_road)

    return cost

n = 6
c_lib = 2
c_road = 5
cities =[[1,3],[3,4],[2,4],[1,2],[2,3],[5,6]]



print(roadsAndLibraries(n, c_lib, c_road, cities))
