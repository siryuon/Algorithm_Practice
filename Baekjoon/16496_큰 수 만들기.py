import sys
def sort(num):
    for i in range(len(num) - 1):
        for j in range(len(num) - i - 1):
            if int(num[j + 1] + num[j]) > int(num[j] + num[j + 1]):
                num[j], num[j + 1] = num[j + 1], num[j]

n = int(sys.stdin.readline())
lst1 = list(sys.stdin.readline().split())
sort(lst1)

print(int(''.join(lst1)))
