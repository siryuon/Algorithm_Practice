import sys

T = int(sys.stdin.readline())
n = []
for _ in range(T):
    n.append(int(sys.stdin.readline()))

arr = [1, 2, 4]
length = len(arr)

for i in range(len(n)):
    while length < n[i]:
        arr.append(sum(arr[-3:])%1000000009)
        length += 1

    print(arr[n[i]-1])
