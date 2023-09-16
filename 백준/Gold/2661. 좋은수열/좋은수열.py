import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())

def check(s): # 나쁜 순열 체크용
    for i in range(1, (len(s) // 2) + 1):
        for j in range(len(s) - (i * 2) + 1):
            if s[j : j + i] == s[i + j : i * 2 + j]:
                return 0
    return 1

def back_tracking(num, N):
    if not check(num):
        return
    if len(num) == N:
        print(num)
        sys.exit()
    else:
        for j in range(1, 4):
            back_tracking(num + str(j), N)

back_tracking('1', N)
