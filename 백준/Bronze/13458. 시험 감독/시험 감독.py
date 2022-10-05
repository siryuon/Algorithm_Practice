import sys

N = int(sys.stdin.readline())
room = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

answer = 0
for i in range(N):
    if room[i] > 0:
        room[i] -= B
        answer += 1

    if room[i] > 0:
        answer += int(room[i]/C)
        if room[i] % C != 0:
            answer += 1
        
print(answer)