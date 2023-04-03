import sys
input = sys.stdin.readline
n, m = map(int, input().split())
node = [list(map(int, input().split())) for _ in range(m)]
distances = [float('inf')] * (n+1)

def bell(start):
    distances[start] = 0
    
    # v-1번 반복
    for c in range(n):
        for i in range(m):
            now, nxt, weight = node[i]
            if distances[now] != float('inf') and distances[nxt] > distances[now] + weight:
                distances[nxt] = distances[now] + weight
                if c == n-1: # 무한루프가 도는 경우
                    return False
    return True

if bell(1): # 1번이 시작점일 경우 만약 무한루프가 안돈다면
    for i in range(2, n+1):
        if distances[i] == float('inf'):
            print(-1)
        else:
            print(distances[i])
else: # 무한루프일경우
    print(-1)