import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
delete_num = int(sys.stdin.readline())

def delete(n, num):
    num[n] = -2
    for i in range(len(num)):
        if n == num[i]:
            delete(i, num)
            
delete(delete_num, num)
cnt = 0

for i in range(len(num)):
    if num[i] != -2 and i not in num:
     cnt += 1

print(cnt)
