import sys

dial = [[],[],[],['ABC'],['DEF'],['GHI'],['JKL'],['MNO'],['PQRS'],['TUV'],['WXYZ']]

alpha = sys.stdin.readline().strip()

result = 0

for a in alpha:
    for i in range(len(dial)):
        if a in str(dial[i]):
            result += i

print(result)
