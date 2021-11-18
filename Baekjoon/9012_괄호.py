import sys

n = int(sys.stdin.readline())

for i in range(n):
    bracket = input()
    sum = 0

    for b in bracket:
        if b == '(':
            sum += 1
        else:
            sum -= 1

        if sum < 0:
            print('NO')
            break

    if sum == 0:
        print('YES')
    elif sum > 0:
        print('NO')
