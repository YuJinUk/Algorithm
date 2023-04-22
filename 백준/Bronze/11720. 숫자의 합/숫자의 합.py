def solution():
    answer = 0
    n = int(input())
    nums = list(input())
    for i in nums: answer += int(i)
    return answer
print(solution())