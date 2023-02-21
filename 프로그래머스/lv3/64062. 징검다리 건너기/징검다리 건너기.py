from collections import deque
def solution(stones, k):
    ans = deque()
    n = len(stones)
    result = deque()
    for i in range(k): # range(3)

        while ans and stones[i] > stones[ans[-1]]:
            ans.pop()
        ans.append(i)
    for i in range(k, n): # range(3, 8)
        result.append(stones[ans[0]])
        
        while ans and ans[0] <= i-k:
            ans.popleft()
        while ans and stones[i] >= stones[ans[-1]]:
            ans.pop()
        ans.append(i)
    result.append(stones[ans[0]])
    return min(result)
# from collections import deque
# def solution(stones, k):
#     max_slide = deque()
#     min_value = 2 * (10**9)
#     for i in stones:
#         if len(max_slide) < k-1:
#             max_slide.append(i)
#             continue
#         max_slide.append(i)
#         max_value = max(max_slide)
#         if min_value > max_value:
#             min_value = max_value
#         max_slide.popleft()
#     return min_value