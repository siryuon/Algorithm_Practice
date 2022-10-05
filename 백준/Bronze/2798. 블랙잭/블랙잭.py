import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
result = 0

for cards in combinations(card, 3):
    tmp = sum(cards)

    if result < tmp <= m:
        result = tmp

print(result)