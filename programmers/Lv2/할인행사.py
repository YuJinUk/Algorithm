def solution(want, number, discount):
    n = sum(number)
    l = len(discount)
    w = len(want)
    result = 0
    for i in range(l-n+1):
        new_list = discount[i:i+n]
        cnt = 0
        for j in range(w):
            if new_list.count(want[j]) == number[j]:
                cnt +=1
        if cnt == w:
            result += 1
    return result