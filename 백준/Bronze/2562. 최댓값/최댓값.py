import sys

lst = []
m = 0

for i in range(9):
    a = int(sys.stdin.readline())
    lst.append(a)

for i in range(9):
    if m < lst[i]:
        m = lst[i]
        idx = i + 1

print(m)
print(idx)