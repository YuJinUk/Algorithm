n, x = map(int, input().split())
nums = list(map(int, input().split()))
answer = []
for i in nums:
    if i < x:
        answer.append(i)
print(*answer)