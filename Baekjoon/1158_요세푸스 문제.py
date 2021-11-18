import sys

N, K = map(int, sys.stdin.readline().split())

lst = list(range(N))

print('<', end = '')
idx = K-1

for i in range(N-1) :
  idx %= N-i
  print(lst.pop(idx)+1, end = ', ')
  idx += K-1
print(lst.pop()+1, end = '>')
