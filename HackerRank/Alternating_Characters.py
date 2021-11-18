def alternatingCharacters(s):
    res = [s[0]]
    ans = 0
    for i in range(1, len(s)):
        if s[i] == res[-1]:
            ans += 1
        else:
            res.append(s[i])
    return ans


a = 'AAABBB'

print(alternatingCharacters(a))
