from collections import defaultdict

def isValid(s):
    char = defaultdict()

    for a in s:
        char[a] += 1
    return char

s = 'aabbccddeefghi'
print(isValid(s))
