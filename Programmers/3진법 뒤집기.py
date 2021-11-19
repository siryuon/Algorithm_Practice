def encode(n):
    three_num = ''
    final = [0, 1, 2]
    while n not in final:
        t = n % 3
        n = n // 3
        three_num = three_num + str(t)
    return three_num + str(n)

def decode(n):
    answer = 0
    for i in range(len(n)-1, -1, -1):
        answer = answer + int(n[i]) * (3 ** (len(n)-1-i))
    
    return answer
    
def solution(n):
    enc = encode(n)
    dec = decode(enc)
    return dec
