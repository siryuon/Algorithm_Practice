import sys

s = sys.stdin.readline().strip()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in cro:
    s = s.replace(c, '*')

print(len(s))
