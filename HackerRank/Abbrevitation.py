def abbreviation(a, b):
    arr = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    arr[0][0] = 1

    for i in range(len(a)):
        for j in range(len(b)+1):
            if arr[i][j]:
                if j < len(b) and a[i].upper() == b[j]:
                    arr[i+1][j+1] = 1
                if a[i].islower():
                    arr[i+1][j] = 1

    return 'YES' if arr[-1][-1] else 'NO'

a = 'beFgH'
b = 'EFG'

print(abbreviation(a, b))
