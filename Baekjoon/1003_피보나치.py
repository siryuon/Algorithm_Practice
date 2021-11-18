T = int(input())

zeroCount = [1, 0]
oneCount = [0, 1]

for i in range(2, 41):
    zeroCount.append(zeroCount[i-1] + zeroCount[i-2])
    oneCount.append(oneCount[i-1] + oneCount[i-2])

for _ in range(T):
    number = int(input())
    print(zeroCount[number], oneCount[number])
