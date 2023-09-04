from collections import deque
def solution(board, moves):
    answer = 0
    stack, dic = [], {}
    for b in board:
        for idx, i in enumerate(b):
            if not i: continue
            if idx+1 not in dic: dic[idx+1] = deque([i])
            else: dic[idx+1].append(i)
    for move in moves:
        if not dic[move]: continue
        nxt = dic[move].popleft()
        if stack and stack[-1] == nxt: answer += 2; stack.pop()
        else: stack.append(nxt)
    return answer