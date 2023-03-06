T = int(input())
for tt in range(1, T+1):
    n, m = map(int, input().split())
    color = [list(input().rstrip()) for _ in range(n)]
    answer = 10**10
    i = 1
    while i<n-1:
        j = i + 1
        while j<n:
            cnt = 0
            for a in range(i):
                cnt_w = color[a].count('W')
                cnt += m - cnt_w
            for b in range(i, j):
                cnt_b = color[b].count('B')
                cnt += m - cnt_b
            for c in range(j, n):
                cnt_c = color[c].count('R')
                cnt += m - cnt_c
            if cnt < answer:
                answer = cnt
            j += 1
        i += 1
    print(f'#{tt} {answer}')