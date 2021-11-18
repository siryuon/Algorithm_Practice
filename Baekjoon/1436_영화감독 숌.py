import sys

n = int(sys.stdin.readline())

movie = 0
cnt = 0

while True:
    movie += 1
    if '666' in str(movie):
        cnt += 1

    if cnt == n:
        break

print(movie)
