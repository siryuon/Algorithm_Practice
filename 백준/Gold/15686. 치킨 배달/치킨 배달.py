from itertools import combinations
import math

N, M = map(int, input().split())
city = []
result = math.inf
for _ in range(N):
    city.append(list(map(int, input().split())))

house = []
chicken_store = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken_store.append([i, j])

for chicken in combinations(chicken_store, M):
    tmp = 0
    for h in house:
        dist = 100
        for j in range(M):
            dist = min(dist, abs(h[0] - chicken[j][0]) + abs(h[1] - chicken[j][1]))
        tmp += dist
    result = min(result, tmp)
    
print(result)