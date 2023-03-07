import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

answer = 0
def solution(a, edges):
    visited = [0 for _ in range(len(a))]
    
    if sum(a) != 0:
        return -1
    
    tree = defaultdict(list)
    
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)
    
    def dfs(x, a, tree, visited):
        global answer
        visited[x] = 1
        
        for y in tree[x]:
            if not visited[y]:
                a[x] += dfs(y, a, tree, visited)
        
        answer += abs(a[x])
        return a[x]
    dfs(0, a, tree, visited)
    return answer
    