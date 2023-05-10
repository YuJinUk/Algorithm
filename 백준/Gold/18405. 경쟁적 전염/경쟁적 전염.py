import sys
input = sys.stdin.readline

n, k = map(int, input().split())
virus = {i : [] for i in range(1, k+1)}

matrix = []

for row in range(n):
    col = list(map(int, input().split()))
    for idx, check in enumerate(col):
        if check:
            virus[check].append((row, idx))
    matrix.append(col)
    
t, x, y = map(int, input().split())

dxdy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0
while not matrix[x-1][y-1] and cnt < t:
    for num, v in virus.items():
        checklist = []
        for cx, cy in v:
            for dx, dy in dxdy:
                nx = cx + dx
                ny = cy + dy
                if -1<nx<n and -1<ny<n and not matrix[nx][ny]:
                    matrix[nx][ny] = num
                    checklist.append((nx, ny))
        virus[num] += checklist
    cnt += 1

print(matrix[x-1][y-1])