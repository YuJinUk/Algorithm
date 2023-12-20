from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    l = len(begin)
    visited = deque()
    visited.append((begin,0))
    result = [False] * (len(words))
    while visited:
        alpha, cnt_alpha = visited.popleft()
        
        if alpha == target:
            break
            
        for j in range(len(words)):
            word = words[j]
            cnt = 0
            
            if not result[j]:
                for i in range(l):
                    if alpha[i] != word[i]:
                        cnt += 1
                        
            if cnt == 1:
                visited.append((word, cnt_alpha+1))
                result[j] = True
                
    return cnt_alpha