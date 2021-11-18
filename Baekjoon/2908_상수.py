import sys

def reverse(num):
    r = str(num)
    return int(r[::-1])
    
n, m = map(int, sys.stdin.readline().split())

n = reverse(n)
m = reverse(m)

print(max(n, m))
