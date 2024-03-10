def solution(storey):
    summ = 0
    while storey != 0:
        mod = storey % 10
        n = (storey // 10) % 10
        if mod >= 6:
            storey += 10 - mod
            summ += 10 - mod
        elif mod == 5 and n >= 5:
            storey += 10 - mod
            summ += 10 - mod
        else:
            summ += mod
        storey = storey//10
    return summ