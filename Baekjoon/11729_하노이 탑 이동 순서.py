import sys

n = int(sys.stdin.readline())

move = []
def hanoi(n, a, b, c):
    if n == 1:
        move.append([a,c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a,c])
        hanoi(n-1, b, a, c)

hanoi(n, 1, 2, 3)

print(len(move))
for i in range(len(move)):
    print(" ".join([str(move[i][0]), str(move[i][1])]))
