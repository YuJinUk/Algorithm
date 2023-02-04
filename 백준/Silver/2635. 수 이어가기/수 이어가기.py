def solution():
    a = int(input())
    if a == 1:
        return 4, [1,1,0,1]
    b = a//2
    num_list = []
    i , j = 1, -1
    num = [1,0]
    result = 0
    while b<a:
        nums = i *num[0]* a + j *num[1]* b
        num[0], num[1] = num[1], num[0] + num[1]
        i, j= j, i
        if nums >= 0:
            num_list.append(nums)
        else:
            if result < len(num_list):
                result = len(num_list)
                result_list = num_list
            b += 1
            num = [1,0]
            num_list = []
    return result, result_list
a,b = solution()
print(a)
print(*b)