import heapq

def solution(n, works):
    ans = 0
    heap = []

    for work in works:
        heapq.heappush(heap, (-work, work))


    print(heap)
    while True:
        if n == 0:
            break
        
        work = heapq.heappop(heap)[1]-1
        heapq.heappush(heap, (-work, work))
        n -= 1

    for h in heap:
        if h[1] < 0:
            continue
        ans += h[1] ** 2
        
    return ans

n = 4
works = [3, 4, 3]

print(solution(n, works))
