# 효율성테스트 345 미통과
# from collections import Counter
# def solution(s):
#     count_list = list(Counter(s).values())
#     for i in count_list: # 하나라도 홀수개수가 있으면 return 0
#         if i % 2 == 1:
#             return 0
        
#     set_s = list(set(s)) # set_s : 원소 구하기
#     for i in range(len(set_s)): # 2개씩 붙은 원소 리스트 구하기
#         set_s[i] = set_s[i]*2
#     while True:
#         first = len(s)
#         for i in set_s:
#             s = s.replace(i,'')
#         second = len(s)
#         if first == second:
#             break
#     if len(s) == 0:
#         return 1
#     else:
#         return 0
    
# Stack을 활용한 풀이.  
from collections import Counter
from collections import deque

def solution(s):
    count_list = list(Counter(s).values())
    for i in count_list: # 하나라도 홀수개수가 있으면 return 0
        if i % 2 == 1:
            return 0

        list_s = deque() # list_s는 append와 pop이 빠른 deque로 생성

    for i in s:
        if len(list_s)==0: # list_s에 원소가 없으면 추가해줌.
            list_s.append(i)
        else: # list_s에 원소가 있다면 다음으로 추가되는 원소와 비교
            if list_s[-1] == i :
                list_s.pop()
            else:
                list_s.append(i)
    if len(list_s)==0:
        return 1
    else:
        return 0