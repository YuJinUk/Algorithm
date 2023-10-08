import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def checking(line):
    for i in range(1, N):
        if abs(line[i] - line[i - 1]) > 1: # 높이 차이가 1보다 큰 경우
            return False
        if line[i] < line[i - 1]: # 좌측이 더 큰 경우
            for j in range(L):
                if i + j >= N or line[i] != line[i + j] or slope[i + j]:
                    return False
                if line[i] == line[i + j]:
                    slope[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(L):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    slope[i - j - 1] = True
    return True


for i in range(N):
    slope = [False] * N
    if checking([graph[i][j] for j in range(N)]):
        answer += 1

for j in range(N):
    slope = [False] * N
    if checking([graph[i][j] for i in range(N)]):
        answer += 1

print(answer)