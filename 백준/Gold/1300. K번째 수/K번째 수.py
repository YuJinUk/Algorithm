N = int(input())
K = int(input())
start, end = 1, N**2
while start <= end:
    mid = (start + end) // 2
    check = 0
    for i in range(1, N + 1):
        check += min(mid // i, N)
    if check >= K:
        end = mid - 1
    else:
        start = mid + 1
print(start)