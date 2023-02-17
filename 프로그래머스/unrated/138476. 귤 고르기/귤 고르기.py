from collections import Counter
def solution(k, t): # k: 총 뽑을 귤의 수, t : 귤 사이즈 리스트 
   cnt_t = Counter(t)
   num = list(cnt_t.values())
   num = sorted(num, reverse = True)
   cnt = 0 #누적
   l = len(num)
   for i in range(l) :
       max_num = num.pop(0)
       cnt += max_num
       if max_num >= k:
           return i+1
           break
       else :
           k -= max_num

# 재귀로 새로 풀어보기
# from collections import Counter
# cnt = 0 # 귤의 종류 수
# def re(a,nums):
#     cnt = 1
#     max_nums = nums[-1]
#     if max_nums >= a: # k보다 max(num)이 크다면 함수가 끝남
#         return cnt
#     else :
#         # nums에서 가장 큰 수를 제거함
#         nums.pop()
#         cnt += re(a-max_nums, nums) # 재귀
#     return cnt
# def solution(k, t): # k: 총 뽑을 귤의 수, t : 귤 사이즈 리스트 
#     cnt_t = Counter(t)
#     num = sorted(list(cnt_t.values()))
#     return re(k,num)
