import sys

N = sys.stdin.readline().strip()
L = int(N[-1])
if L == 2 or L == 5 or L == 7 or L == 0:
    print('CY')
else:
    print('SK')
