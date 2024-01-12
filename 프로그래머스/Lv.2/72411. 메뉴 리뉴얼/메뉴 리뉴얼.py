from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for cour in course:
        dic = defaultdict(int)
        for order in orders:
            order = sorted(list(order))
            for lst in list(combinations(order, cour)):
                x = ''.join(lst)
                dic[x] += 1
        if dic.values():
            max_order = max(dic.values())
            if max_order < 2:
                continue
            for i in dic:
                if dic[i] == max_order:
                    answer.append(i)
    return sorted(answer)