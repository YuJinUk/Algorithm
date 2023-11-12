s_list = [0,0]

def solution(s):
    global s_list
    l = len(s)
    if s == '1':
        return s_list
    
    count_s = s.count('1')
    s_list[1] += l - count_s
    s = bin(count_s)[2:]
    s_list[0] += 1
    return solution(s)