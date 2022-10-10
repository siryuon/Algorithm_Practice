import sys, math

N = int(sys.stdin.readline())

def isPrime(x):
    if x == 1:
        return False
    
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False

    return True

def isPalindrome(x):
    x = str(x)
    tmp = x[::-1]

    if x == tmp:
        return True
    else:
        return False
    
answer = 0

while True:
    if isPalindrome(N):
        if isPrime(N):
            print(N)
            break
    N += 1