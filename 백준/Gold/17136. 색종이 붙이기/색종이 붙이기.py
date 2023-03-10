def check(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if not checkboard[i][j]:
                return 1
    return 0

def changeto0(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            checkboard[i][j] = 0
    return

def changeto1(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            checkboard[i][j] = 1
    return

checkboard = [list(map(int, input().split())) for _ in range(10)]
checkcnt = [0] + [5] * 5
answer = 26
def sq():
    global answer
    # print(checkcnt)
    # print(checkboard)
    if 1 not in sum(checkboard,[]):
        answer = min(answer, 26 - sum(checkcnt))
        return
    for i in range(10):
        for j in range(10):
            if not checkboard[i][j]:
                continue
            # print([i,j])
            for k in range(5, 0, -1):
                if i+k>10 or j+k>10:
                    continue
                if not checkcnt[k]:
                    continue
                if check(i,j,k):
                    continue
                checkcnt[k] -= 1
                changeto0(i, j, k)
                sq()
                checkcnt[k] += 1
                changeto1(i, j, k)
            return
sq()

if answer == 26:
    print(-1)
else:
    print(answer-1)