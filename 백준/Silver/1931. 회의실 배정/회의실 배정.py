import sys

n = int(sys.stdin.readline())
conf = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    conf.append((s, e))

conf = sorted(conf, key=lambda x:x[0])
conf = sorted(conf, key=lambda x:x[1])

cnt = 0
start_time = 0

for time in conf:
    if time[0] >= start_time:
        start_time = time[1]
        cnt +=1

print(cnt)