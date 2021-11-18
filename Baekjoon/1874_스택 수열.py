import sys

n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

stack, result, cnt = [], [], 1
dead = False
for l in lst:
    while cnt <= l:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    if stack.pop() != l:
        print('NO')
        dead = True
        break
    else:
        result.append('-')
        
if not dead:
    print('\n'.join(result))
