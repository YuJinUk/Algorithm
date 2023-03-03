from collections import deque
def solution(s):
    result = deque()
    for st in s:
        cnt = 0
        stack = deque()
        st_list = deque(list(st))
        while st_list:
            alpha = st_list.popleft()
            if len(stack)<2:
                stack.append(alpha)
                continue
            if alpha == "0" and stack[-1] == "1" and stack[-2] == "1":
                stack.pop()
                stack.pop()
                cnt += 1
                continue
            stack.append(alpha)
        st = "".join(stack)
        if "0" not in st:
            answer = "110"*cnt + st
            result.append(answer)
            continue
        for i in range(len(st)-1,-1,-1):
            if st[i] == "0":
                answer = st[:i+1] + "110"*cnt + st[i+1:]
                result.append(answer)
                break
    return list(result)