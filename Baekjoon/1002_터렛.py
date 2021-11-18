n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

    radiusList = [r1, r2, r]
    maxRadius = max(radiusList)
    radiusList.remove(maxRadius)
    
    if r == 0 and r1 == r2:
        print(-1)
    elif r == r1+r2 or maxRadius == sum(radiusList):
        print(1)
    elif maxRadius > sum(radiusList):
        print(0)
    else:
        print(2)
