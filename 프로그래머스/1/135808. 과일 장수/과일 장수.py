def solution(k, m, score):
    score = sorted(score, reverse=True)
    return sum([score[i]*m for i in range(m-1, len(score), m)])