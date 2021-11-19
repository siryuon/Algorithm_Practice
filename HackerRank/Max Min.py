import math

def maxMin(k, arr):
    arr.sort()
    diff = []
    res = 0
    mn = math.inf
    
    for i in range(len(arr)-1):
        diff.append(arr[i+1] - arr[i])
        
    for i in range(k-1):
        res += diff[i]
    print(res)
    mn = res

    for i in range(k-1, len(diff)):
        res -= diff[i-(k-1)]
        res += diff[i]

        if mn > res:
            mn = res

    return mn

k = 3
arr = [10, 100, 300, 200, 1000, 20, 30]

print(maxMin(k, arr))
