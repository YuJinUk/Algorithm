import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    max_heap, min_heap = [], []
    visit = [False] * 1_000_001

    for key in range(int(input())):
        x, y = input().rsplit()
        if x == 'I':
            heapq.heappush(min_heap, (int(y), key))
            heapq.heappush(max_heap, (int(y) * -1, key))
            visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif x == 'D':
            if y == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap:
                    visit[min_heap[0][1]] = False # visit이 Ture였으므로 False로 바꾸고 삭제
                    heapq.heappop(min_heap)
            elif y == '1':
                while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')