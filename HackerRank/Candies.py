def candies(n, arr):

    candy = [1] * n

    for i in range(n-1):
        if arr[i] < arr[i+1]:
            candy[i+1] = candy[i] + 1

    for j in range(n-1, 0, -1):
        if arr[j] < arr[j-1] and candy[j] >= candy[j-1]:
            candy[j-1] = candy[j] + 1

    return sum(candy)

n = 10
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]

print(candies(n, arr))
