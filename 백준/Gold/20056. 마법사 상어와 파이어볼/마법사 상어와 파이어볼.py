import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = [[[] for _ in range(N)] for _ in range(N)]

# r, c, m, s, d 순서
fireball = []
rc = []
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireball.append((r-1, c-1, m, s, d))
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def dfs(count_number, fireballs):
    if count_number == K:
        answer = 0
        for i in fireballs:
            answer += i[2]
        print(answer)
        return
    # 이동해서 matrix에 넣기
    while fireballs:
        r, c, m, s, d = fireballs.pop(0)
        x = (r + s * direction[d][0]) % N
        y = (c + s * direction[d][1]) % N
        matrix[x][y].append([m, s, d])
    # 2개이상 있는 곳 작업
    for i in range(N):
        for j in range(N):
            if not matrix[i][j]:
                continue
            if len(matrix[i][j]) == 1:
                fireballs.append([i, j] + matrix[i][j].pop())
                continue
            l = len(matrix[i][j])
            summ, sums = 0, 0
            odd, even = 0, 0
            while matrix[i][j]:
                m, s, d = matrix[i][j].pop(0)
                summ += m
                sums += s
                if d % 2:
                    odd += 1
                else:
                    even += 1
            if not summ // 5: continue
            if not even or not odd: d = [0, 2, 4, 6]
            else: d = [1, 3, 5, 7]
            for dd in d:
                fireballs.append([i, j, summ//5, sums//l, dd])
    dfs(count_number + 1, fireballs)

dfs(0, fireball)