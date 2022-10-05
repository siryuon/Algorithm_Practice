import sys

N = sys.stdin.readline().strip()

def solution(N):
    nums = []
    numsum = 0
    ans = 0
    
    for i in N:
        nums.append(int(i))
        numsum += int(i)

    nums.sort(reverse=True)
    if nums[-1] != 0 :
       return -1
    elif numsum % 3 != 0 :
       return -1
    else :
        for i in nums:
            ans *= 10
            ans += i
            
    return ans

print(solution(N))