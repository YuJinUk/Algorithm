def solution(picks, minerals):
    answer = 0
    l = len(minerals)
    if l <= picks[0] * 5 :
        return l
    div = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]
    dic = {'diamond': 25, 'iron': 5, 'stone': 1}
    check, score = [], []
    for idx, d in enumerate(div):
        x = [dic[i] for i in d]
        check.append(x)
        score.append((sum(x), idx))
    if sum(picks) < len(check):
        check = check[:sum(picks)]
        score = score[:sum(picks)]
    score.sort()
    while score:
        if picks == [0, 0, 0]:
            break
        x, xidx = score.pop()
        if picks[0]:
            picks[0] -= 1
            answer += len(check[xidx])
            continue
        if picks[1]:
            picks[1] -= 1
            for i in check[xidx]:
                if i == 25:
                    answer += 5
                else:
                    answer += 1
            continue
        if picks[2]:
            picks[2] -= 1
            for i in check[xidx]:
                if i == 25:
                    answer += 25
                elif i == 5:
                    answer += 5
                else:
                    answer += 1
            continue
    return answer