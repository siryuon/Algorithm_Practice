import sys

n = int(sys.stdin.readline())
lst1 = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

def search(n, lst, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    
    if n == lst[mid]:
        return 1
    elif n < lst[mid]:
        end = mid - 1
    elif n > lst[mid]:
        start = mid + 1

    return search(n, lst, start, end)
        
for num in lst2:
    print(search(num, lst1, 0, len(lst1) - 1)) 
