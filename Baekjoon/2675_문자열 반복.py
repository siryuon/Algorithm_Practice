import sys

t = int(sys.stdin.readline())

for i in range(t):
    result = ''
    r, s = sys.stdin.readline().split()
    for j in s:
        result += j * int(r)
    print(result)
