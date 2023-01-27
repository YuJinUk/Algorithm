s_list = [0,0]

def solution(s):
    global s_list
    l = len(s)
    if s == '1': #만약 1만남으면 return
        return s_list
    
    count_s = s.count('1') #1의 개수 : 0을 지우고 길이구함.
    s_list[1] += l - count_s
    s = bin(count_s)[2:] # 2진법으로 변환
    s_list[0] += 1
    return solution(s) # 재귀