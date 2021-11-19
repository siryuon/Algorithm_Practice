def solution(numbers):
    number = [str(num) for num in numbers]
    number.sort(key=lambda num: num*3, reverse=True)
    
    return str(int(''.join(number)))
    
numbers=[3,30,34,5,9]

print(solution(numbers))
