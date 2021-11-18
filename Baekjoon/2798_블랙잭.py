import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

lst = list(permutations(card, 3))
sums = []

for i in range(len(lst)):
    sums.append(sum(lst[i]))    
sums = sorted(sums, reverse=True)
for i in range(len(sums)):
    answer = sums[i]
    
    if answer <= m:
        break

print(answer)
