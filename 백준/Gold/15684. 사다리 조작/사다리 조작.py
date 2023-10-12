import sys
input = sys.stdin.readline

def check():
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if lines[j][now] == 1:
                now += 1
            elif lines[j][now - 1] == 1:
                now -= 1
        if i != now:
            return False
    return True

def solution(added, num):
    global answer
    if added >= answer:
        return
    if check():
        answer = added
        return
    for idx in range(num + 1, len(add_list)):
        i, j = add_list[idx]
        if lines[i][j - 1] == 0 and lines[i][j + 1] == 0:
            lines[i][j] = 1
            solution(added + 1, idx)
            lines[i][j] = 0

N, M, H = map(int, input().split())
lines = [[0 for _ in range(N + 1)] for _ in range(H + 1)]
add_list = []
for _ in range(M):
    x, y = map(int, input().split())
    lines[x][y] = 1
for i in range(1, H + 1):
    for j in range(1, N):
        if not lines[i][j] and not lines[i][j - 1] and not lines[i][j + 1]:
            add_list.append([i, j])
            
answer = 4
solution(0, -1)
print(answer if answer < 4 else -1)
