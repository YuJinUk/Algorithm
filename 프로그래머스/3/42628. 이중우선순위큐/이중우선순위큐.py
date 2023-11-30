import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    for a in operations:
        alpha, num = a.split()
        num = int(num)
        if alpha == 'I':
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif alpha == 'D':
            if num == 1 and max_heap:
                heapq.heappop(max_heap)
                min_heap.pop()
            elif num == -1 and min_heap:
                heapq.heappop(min_heap)
                max_heap.pop()
    if max_heap and min_heap:
        max_num = heapq.heappop(max_heap)
        min_num = heapq.heappop(min_heap)
        if max_num * -1 >= min_num:
            return [max_num * -1, min_num]
    else:
        return [0,0]