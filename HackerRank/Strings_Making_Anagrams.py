from collections import defaultdict

def makeAnagram(a, b):
    word = defaultdict(int)

    for c in a:
        word[c] += 1
    for c in b:
        word[c] -= 1

    return sum(abs(x) for x in word.values() if x)
    

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

print(makeAnagram(a, b))
