import sys

while(True):
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        m = int(str(n)[::-1])

    if n == m:
        print("yes")
    else:
        print("no")
