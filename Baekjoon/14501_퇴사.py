import sys

N = int(sys.stdin.readline())
t = []
p = []
arr = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)
    arr.append(b)

arr.append(0)

for i in range(N-1, -1, -1):
    if t[i] + i > N:
        arr[i] = arr[i+1]
    else:
        arr[i] = max(arr[i+1], p[i] + arr[i+t[i]])

print(arr[0])
