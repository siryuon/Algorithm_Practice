M = int(input())
N = int(input())

primeSum = 0
minimum = 10000

def prime(number):
    bucket = []
    number = int(number)
    
    if number == 1:
        return False
    
    for i in range(1, number + 1):
        if number % i == 0:
            bucket.append(i)

    if len(bucket) == 2:
        return True
    else:
        return False
    
for number in range(M, N + 1):
    if prime(number):
        primeSum += number
        if number < minimum:
            minimum = number

if primeSum == 0:
    print(-1)
else:
    print(primeSum)
    print(minimum)   
