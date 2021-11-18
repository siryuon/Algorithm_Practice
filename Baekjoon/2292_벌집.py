import sys

a = int(sys.stdin.readline())
start = 1
circle = 0
cnt = 0

while True:
    start += circle
    cnt += 1
    if a <= start:
        print(cnt)
        break
    circle += 6
