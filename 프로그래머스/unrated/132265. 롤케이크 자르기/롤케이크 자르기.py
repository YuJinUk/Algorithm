from collections import deque
from collections import Counter
def solution(topping):
    result = 0
    topping = deque(topping)
    left_set = set()
    right_dic = dict(Counter(topping))
    for idx in topping:
        left_set.add(idx)
        right_dic[idx] -= 1
        if right_dic[idx] == 0:
            del right_dic[idx]
        if len(left_set) == len(right_dic):
            result += 1
    return result