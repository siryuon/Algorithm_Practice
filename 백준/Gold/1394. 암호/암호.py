import sys
from collections import defaultdict

input = sys.stdin.readline

lst = input().strip()
password = input().strip()

dic = defaultdict()

cnt = 0
for l in lst:
    cnt += 1
    dic[l] = cnt

ans, flag = 0, 1

for i in range(len(password)-1, -1, -1):
    ans = (ans + flag * dic[password[i]]) % 900528
    flag = flag * len(lst) % 900528

print(ans)