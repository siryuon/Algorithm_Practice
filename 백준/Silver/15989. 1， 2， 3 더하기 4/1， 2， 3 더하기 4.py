import sys

T = int(sys.stdin.readline())
arr = [1] * 10001

for i in range(2, 10001):
    arr[i] += arr[i-2]
    
for i in range(3, 10001):
    arr[i] += arr[i-3]
    
for _ in range(T):
    n = int(sys.stdin.readline())
    print(arr[n])