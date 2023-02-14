# 2805 농작물 수확하기
T = int(input())
for tt in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(n)]
    result = []
    rm = n//2
    for idx, i in enumerate(matrix):
        m = abs(rm - idx)
        for k in range(m):
            i.pop()
            i.pop(0)
        result.append(i)
    ans = 0
    for i in result:
        ans += sum(i)
    print(f'#{tt} {ans}')