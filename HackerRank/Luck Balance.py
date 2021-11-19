import heapq

def luckBalance(k, contests):
    ans = 0
    imp, unimp = [], []
    
    for luck, i in contests:
        if i == 1:
            heapq.heappush(imp, -luck)
        else:
            heapq.heappush(unimp, luck)

    for _ in range(k):
        try:
            ans += (heapq.heappop(imp) * -1)
            print(ans)
        except:
            continue
    
    ans += sum(unimp)
    ans += sum(imp)
    return ans

k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

print(luckBalance(k, contests))
