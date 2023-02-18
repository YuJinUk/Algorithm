from collections import deque
def solution(arr, K):
    Qi = deque()
    N = len(arr)
    result = deque()
    for i in range(K):

        while Qi and arr[i] > arr[Qi[-1]]:
            Qi.pop()

        Qi.append(i)
    for i in range(K, N):
        result.append(arr[Qi[0]])
        while Qi and Qi[0] <= i-K:
            Qi.popleft()
        while Qi and arr[i] >= arr[Qi[-1]]:
            Qi.pop()
        Qi.append(i)
    result.append(arr[Qi[0]])
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