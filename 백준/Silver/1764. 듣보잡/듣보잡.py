import sys

N, M = map(int, sys.stdin.readline().split())

hear = set()
see = set()

for _ in range(N):
    hear.add(sys.stdin.readline().strip())
    
for _ in range(M):
    see.add(sys.stdin.readline().strip())

result = sorted(hear&see)

print(len(result))
print('\n'.join(sorted(result)))