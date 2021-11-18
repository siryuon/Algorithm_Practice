import sys

def han(n):
    num = []
    
    for i in str(n):
        num.append(int(i))

    for i in range(len(num) - 1):
        if i == 0:
            gap = num[i] - num[i+1]
        else:
            if gap != (num[i] - num[i+1]):
                return False

    return True
            
n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n+1):
    if han(i):
        cnt += 1

print(cnt)
