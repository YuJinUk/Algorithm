from collections import deque
def cal(x, y, z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    else:
        if x < 0:
            return -(abs(x) // y)
        else:
            return x // y
a = ['+', '-', '*', '/']

for tc in range(1, int(input()) + 1):
    n = int(input())
    aa = list(map(int, input().split()))
    # check = deque()
    # for idx, i in enumerate(aa):
    #     for j in range(i):
    #         check.append(a[idx])
    # print(check)
    nums = list(map(int, input().split()))
    max_check = float('-inf')
    min_check = float('inf')
    visit = [False] * n
    
    def dfs(num, depth = 0):
        global max_check, min_check
        if depth == n-1:
            if max_check < num:
                max_check = num
            if min_check > num:
                min_check = num
            return
        depth += 1
        for i in range(4):
            if aa[i]:
                aa[i] -= 1
                dfs(cal(num, nums[depth], a[i]), depth)
                aa[i] += 1
    
    dfs(nums[0])
    # print(max_check)
    # print(min_check)
    print(f'#{tc} {max_check - min_check}')