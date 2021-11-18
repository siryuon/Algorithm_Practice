import sys

X = int(sys.stdin.readline())
num_list = []

num, cnt = 0, 0

while cnt < X:
    num += 1
    cnt += num

cnt -= num

if num % 2 == 0:
    i = X - cnt
    j = num - i + 1
else:
    i = num - (X - cnt) + 1
    j = X - cnt

print(f'{i}/{j}')
