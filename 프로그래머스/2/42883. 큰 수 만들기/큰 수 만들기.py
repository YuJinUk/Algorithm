# from itertools import combinations
# def solution(num, k):
#     l = len(num)
#     idx = [i for i in range(l)] # 0~l까지 뽑을 idx list
#     idx_list = list(combinations(idx, l-k)) # l-k개의 모든 조합
#     result = []
#     for i in idx_list:
#         li = ''
#         for j in range(l-k):
#             li += str(num[i[j]])
#         result.append(li)
#     return sorted(result)[-1]

def solution(num, k):
    stack = [] 
    for nums in num:
        while stack and stack[-1] < nums and k > 0:
            stack.pop()
            k -= 1
        stack.append(nums)
        
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)