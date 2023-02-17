# dfs
from collections import deque
def solution(k, d): # d : dungeons
    l, n, dq = len(d), 0, deque()
    dq.append([k, []]) # []는 방문한 곳을 추가하기 위한 공백 리스트
    while dq:
        k, visited = dq.pop()
        for i in range(l): # in d로 안하는 이유는 같은 조건의 던전이 있을 수 있기 때문
            need, use = d[i]
            if i not in visited and k>= need and k-use >=1:
                dq.append([k-use, visited+[i]])
            else :
                n = max(n, len(visited))
    return n