def solution(scores):
    wanho = scores[0]
    if len(scores) == 1:
        return 1
    scores.sort(key=lambda x: -(x[0] + x[1]))
    idx = scores.index(wanho)
    scores = scores[:idx]
    scores.sort(key = lambda x: (-x[0], x[1]))
    max_1 = 0
    ans = 0
    for ids, score in enumerate(scores):
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        if max_1 < score[1]:
            max_1 = score[1]
        elif max_1 > score[1]:
            ans += 1
    return idx + 1 - ans