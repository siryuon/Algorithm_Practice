def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]
    
    n1, n2 = arr[0], max(arr[:2])

    for a in arr[2:]:
        n3 = max(n2, n1+a, a)
        n1, n2 = n2, n3
        
    return n3


arr = [3, 7, 4, 6, 5]
print(maxSubsetSum(arr))

