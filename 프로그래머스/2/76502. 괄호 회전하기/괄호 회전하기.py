from collections import deque
def solution(s):
    l = len(s)
    cnt = 0

    while l > 0:
        l -= 1
        new_s = s[l:] + s[:l]
        s_list = deque()
        for i in new_s:
            if len(s_list) == 0:
                s_list.append(i)
            else :
                if s_list[-1] == '(' and i == ')':
                    s_list.pop()
                elif s_list[-1] == '[' and i == ']':
                    s_list.pop()
                elif s_list[-1] == '{' and i == '}':
                    s_list.pop()
                else :
                    s_list.append(i)
        if len(s_list) == 0:
            cnt += 1
        
    return cnt