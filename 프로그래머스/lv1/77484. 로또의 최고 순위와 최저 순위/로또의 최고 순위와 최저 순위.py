def solution(lottos, win_nums):
    yes, zero = 0, 0
    yeslst, answer = [], []
    for lotto in lottos:
        if lotto and lotto in win_nums: yes += 1; yeslst.append(lotto)
        elif not lotto: zero += 1
    if zero + yes < 2: answer.append(6)
    else: answer.append(7 - (zero + yes))
    if yes < 2 : answer.append(6)
    else: answer.append(7 - yes)
    return answer