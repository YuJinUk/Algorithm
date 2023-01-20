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