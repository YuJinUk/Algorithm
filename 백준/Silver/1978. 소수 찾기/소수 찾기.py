def sosu(n):
    if n == 1:
        return 0
    check = 0
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            check += 2
    if not check:
        return 1
    return 0
n = int(input())
nums = list(map(int, input().split()))
answer = 0
for i in nums:
    answer += sosu(i)
print(answer)