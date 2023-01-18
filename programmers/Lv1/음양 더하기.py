def solution(absolutes, signs):
    sum_num = sum(absolutes)
    for i in range(len(signs)):
        if not signs[i]:
            sum_num -= absolutes[i] * 2
    return sum_num