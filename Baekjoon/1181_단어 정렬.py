import sys

N =int(sys.stdin.readline())
lst = []
result = []

for _ in range(N):
    word = sys.stdin.readline().strip()
    lst.append((word, len(word)))
               
lst = sorted(lst, key=lambda x: (x[1],x[0]))

for l in lst:
    if l[0] not in result:
        result.append(l[0])

for r in result:
    print(r)
