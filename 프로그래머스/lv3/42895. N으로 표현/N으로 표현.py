def solution(N, number):
    dp = [set([int(str(N) * i)]) for i in range(1, 9)]
    
    for i in range(8):
        for j in range(i):
            for n1 in dp[j]:
                for n2 in dp[i-j-1]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0:
                        dp[i].add(n1 // n2)
        
        if number in dp[i]:
            return i + 1
    return -1