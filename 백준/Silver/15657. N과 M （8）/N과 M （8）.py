n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
answer = []

def dfs(d, idx):
    if d == m:
        print(*answer)
        return
    for i in range(idx, n):
        answer.append(nums[i])
        dfs(d + 1, i)
        answer.pop()
dfs(0, 0)