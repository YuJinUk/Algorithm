def solution(e, starts):
    check = [1] * (e+1)
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            check[j] += 1
    max_num = 0
    for idx in range(e,0,-1):
        if check[idx] >= max_num:
            max_num = check[idx]
            check[idx] = idx
        else:
            check[idx] = check[idx+1]
    return [check[i] for i in starts]
# from collections import deque
# def solution(e, starts):
    
#     check = [1] * (e+1)
#     for i in range(2, e + 1):
#         for j in range(i, e + 1, i):
#             check[j] += 1
#     result = []
#     result = deque()
#     for k in range(min(starts), e+1):
#         result.append((check[k],k))
#     result.sort(key = lambda x: -x[0])
#     # result = sorted(result, key = lambda x: -x[0])
    
#     ans = []
#     ans = deque()
#     for start in starts:
#         for div_cnt, div in result:
#             if start <= div:
#                 ans.append(div)
#                 break
#     return ans
# 약수의 개수
# def divisor(n):
#     cnt = 2
#     if (int(n**0.5))**2 != n:
#         for i in range(2, int(n**0.5)+1):
#             if not n % i:
#                 cnt += 2
#         return cnt
#     else:
#         for i in range(2, int(n**0.5)+1):
#             if not n % i:
#                 cnt += 2
#         return cnt-1
#     ans = []
#     for num in starts:
#         max_num = [0,0]
#         for i in range(num, e+1):
#             if not check[i]:
#                 check[i] = divisor(i)
#             if max_num[0] < check[i]:
#                 max_num = [check[i],i]
#         ans.append(max_num[1])
#     return ans