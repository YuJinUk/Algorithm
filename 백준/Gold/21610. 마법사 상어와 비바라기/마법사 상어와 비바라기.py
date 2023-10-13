import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)] # N by N matrix / 각 칸의 값은 바구니 속 물의 양
ds = [list(map(int, input().split())) for _ in range(M)]

# 첫째 줄에 M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 출력한다.

direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# 구름이 이동하는 함수
def move_cloud(cloudlist, di, si):
    dx, dy = direction[di - 1]
    new_cloud_location = []
    for x, y in cloudlist:
        nx, ny = x + dx * si, y + dy * si
        while nx < 0:
            nx += N
        while nx > N - 1:
            nx -= N
        while ny < 0:
            ny += N
        while ny > N - 1:
            ny -= N
        new_cloud_location.append((nx, ny))
    return new_cloud_location

# 구름 비가 내리는 함수
def rain(cloudlist):
    for x, y in cloudlist:
        matrix[x][y] += 1

# 대각선 체크해서 더해주는 함수
def diagonal(cloudlist):
    diagonal_direction = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for x, y in cloudlist:
        yes_cnt = 0
        for dx, dy in diagonal_direction:
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and matrix[nx][ny]:
                yes_cnt += 1
        matrix[x][y] += yes_cnt

# 새로운 구름 생성하는 함수
def new_cloud(cloudlist):
    new_cloudlist = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] >= 2 and (i, j) not in cloudlist:
                matrix[i][j] -= 2
                new_cloudlist.append((i, j))
    return new_cloudlist

first_cloudlist = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for d, s in ds:
    first_cloudlist = move_cloud(first_cloudlist, d, s)
    rain(first_cloudlist)
    diagonal(first_cloudlist)
    first_cloudlist = new_cloud(first_cloudlist)

answer = 0
for i in range(N):
    for j in range(N):
        answer += matrix[i][j]
print(answer)