origin = [i for i in range(1,10001)]
selfnum = []

def self(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

for num in origin:
    if self(num) not in selfnum:
        selfnum.append(self(num))

result = [x for x in origin if x not in selfnum]

for num in result:
    print(num)
