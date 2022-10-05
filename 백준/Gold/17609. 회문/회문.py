import sys

n = int(sys.stdin.readline())

def check(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def palindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            chk1 = check(s, left+1, right)
            chk2 = check(s, left, right-1)

            if chk1 or chk2:
                return 1
            else:
                return 2

    return 0
    
        
for i in range(n):
    s = sys.stdin.readline().strip()
    print(palindrome(s, 0, len(s)-1))