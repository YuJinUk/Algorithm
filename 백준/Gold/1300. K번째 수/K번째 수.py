# 프로그래머스 처리가능한 손님 수
n = int(input())
k = int(input())
start, end = 1, n**2
while start <= end:
    mid = (start + end) // 2
    check = 0
    for i in range(1, n+1):
        check += min(mid//i, n)
    if check >= k:
        end = mid - 1
    else:
        start = mid + 1
print(start)