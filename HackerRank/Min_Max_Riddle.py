#Timeout
def riddle(arr):
    ans = []
    
    for w in range(1, len(arr)+1):
        max_v = 0
        for i in range(len(arr)):
            try:
                if max_v < min(arr[i:i+w]) and len(arr[i:i+w]) == w:
                    max_v = min(arr[i:i+w])
            except:
                continue

        ans.append(max_v)
    return ans

a = [1, 2, 3, 5, 1, 13, 3]

print(riddle(a))
