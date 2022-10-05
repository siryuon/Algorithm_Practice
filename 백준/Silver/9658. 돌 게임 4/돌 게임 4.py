import sys

N = int(sys.stdin.readline())

if N % 7 == 1 or N % 7 == 3:
    print('CY')
else:
    print('SK')