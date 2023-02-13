T = int(input())
for tt in range(1, T+1):
    n, m = map(int, input().split())
    n_num = list(map(int, input().split()))
    m_num = list(map(int, input().split()))
    if n > m:
        n, m = m, n
        n_num, m_num = m_num, n_num
    result = []
    for i in range(m-n+1):
        num = 0
        for j,k in zip(n_num, m_num[i:i+n]):
            num += j * k
        result.append(num)
    print(f'#{tt} {max(result)}')