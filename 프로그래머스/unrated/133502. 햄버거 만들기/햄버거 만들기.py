# ingredient = {
#     1 : '빵',
#     2 : '야채',
#     3 : '고기'
#     }
from collections import deque
def solution(ingredient):
    answer = 0
    stack = []
    check = [1, 2, 3, 1]
    ingredient = deque(ingredient)
    while ingredient:
        ele = ingredient.popleft()
        if len(stack) < 4:
            stack.append(ele)
            continue
        if stack[-4:] == check:
            for _ in range(4):
                stack.pop()
            answer += 1
        stack.append(ele)
    if stack[-4:] == check:
        answer += 1
    return answer