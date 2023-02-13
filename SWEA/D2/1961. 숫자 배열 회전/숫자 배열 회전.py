T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    a_90 = [list(str(arr[n-i-1][j]) for i in range(n)) for j in range(n)]
    a_90_merge = [''.join(a_90[i]) for i in range(n)]
    a_180 = [list(str(arr[n-j-1][n-i-1]) for i in range(n)) for j in range(n)]
    a_180_merge = [''.join(a_180[i]) for i in range(n)]
    a_270 = [list(str(arr[i][n-j-1]) for i in range(n)) for j in range(n)]
    a_270_merge = [''.join(a_270[i]) for i in range(n)]
    print('#%d' %test_case)
    for k in range(n):
        print('%s %s %s' %(a_90_merge[k], a_180_merge[k], a_270_merge[k]))