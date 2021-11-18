N = int(input())
numbers = input().split()

count = 0

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
    
for number in numbers:
    if prime(number):
        count += 1

print(count)
