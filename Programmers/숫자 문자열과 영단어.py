def solution(s):
    alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    ans = ''

    for idx, num in enumerate(alpha):
        if num in s:
            s=s.replace(num, str(idx))
        ans=s

    return int(ans)
