import sys, heapq
input = sys.stdin.readline

maxheap, minheap = [], []
for idx in range(int(input())):
    nxt = int(input())
    if len(maxheap) == len(minheap): heapq.heappush(maxheap, -nxt)
    else: heapq.heappush(minheap, nxt)
    
    if minheap:
        maxx = heapq.heappop(maxheap)
        minn = heapq.heappop(minheap)
        if minn < -maxx:
            heapq.heappush(maxheap, -minn)
            heapq.heappush(minheap, -maxx)
        else:
            heapq.heappush(maxheap, maxx)
            heapq.heappush(minheap, minn)
            
    p = -heapq.heappop(maxheap)
    print(p)
    heapq.heappush(maxheap, -p)