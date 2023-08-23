from collections import Counter
def solution(N, stages):
    result, answer, AllPass = [], [0 for _ in range(N)], 0
    for i in stages:
        if i > N: AllPass += 1; continue
        answer[i-1] += 1
    for i in range(N):
        if not sum(answer[i:]): answer[i] = 0; continue
        answer[i] = answer[i]/(sum(answer[i:]) + AllPass)
    for i in range(N):
        x = answer.index(max(answer))
        result.append(x+1)
        answer[x] = -1
    return result