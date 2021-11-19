import heapq

def solution(scoville, K):
    heap = []
    ans = 0
    for s in scoville:
        heapq.heappush(heap, s)

    while True:
        if len(heap) == 1 and heap[0] < K:
            return -1
        if len(heap) == 1 and heap[0] >= K:
            return ans
        
        first, second = heapq.heappop(heap), heapq.heappop(heap)
        if first >= K:
            heapq.heappush(heap, first)
            heapq.heappush(heap, second)
            break
        else:
            heapq.heappush(heap, first+second*2)
            ans += 1

    return ans

scoville = [1, 1, 100]
K = 7

print(solution(scoville, K))
