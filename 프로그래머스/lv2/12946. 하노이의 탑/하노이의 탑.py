from collections import deque
def solution(n):
    dp = deque([[[1,2]],[[1,2],[1,3],[2,3]]])
    if n<3:
        return dp[n-1]
    for i in range(2, n):
        prior = dp[i-1]
        first = []
        second = []
        for a,b in prior:
            if a == 2 : a = 3
            elif a == 3: a = 2
            if b == 2 : b = 3
            elif b == 3 : b = 2
            first.append([a,b])
        for a,b in prior:
            if a == 2 : a = 1
            elif a == 1 : a = 2
            if b == 2 : b = 1
            elif b == 1 : b = 2
            second.append([a,b])
        dp.append(first+[[1,3]]+second)
    return dp[-1]