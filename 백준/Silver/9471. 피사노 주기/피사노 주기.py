import sys

p = int(sys.stdin.readline())

def fibo(n):
    if len(fibo_list) > n:
        return fibo_list[n]
    else:
        fibo_list[n] = (fibo(n-1) + fibo(n-2)) % m
        return fibo_list[n]

def cycle():
    x = 1
    while True:
        if fibo_list[x] == 0 and fibo_list[x-1] == 1:
            return x
        x += 1
        fibo(x)
        
for _ in range(p):
    fibo_list = dict()
    fibo_list[0] = 0
    fibo_list[1] = 1
    fibo_list[2] = 1
    n, m = map(int, sys.stdin.readline().split())

    print(n, cycle())