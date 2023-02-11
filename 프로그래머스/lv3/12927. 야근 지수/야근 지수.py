import heapq
def solution(n, works):
    sum_work = sum(works)
    if sum_work <= n:
        return 0
    result = []
    for i in works:
        heapq.heappush(result, -i)
    for _ in range(n):
        a = heapq.heappop(result)
        heapq.heappush(result, a+1)
    ans = 0
    for i in range(len(result)):
        a = heapq.heappop(result)
        ans += a**2
    return ans