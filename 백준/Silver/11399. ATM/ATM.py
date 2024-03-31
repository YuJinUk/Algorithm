import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
P = list(map(int, input().split()))
heapq.heapify(P)
answer = 0
for i in range(N):
    x = heapq.heappop(P)
    answer += x * (N - i)
print(answer)