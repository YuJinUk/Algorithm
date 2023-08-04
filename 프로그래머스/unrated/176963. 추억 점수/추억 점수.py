def solution(name, yearning, photo):
    answer, dic = [], {}
    for i, j in zip(name, yearning):
        dic[i] = j
    for name_list in photo:
        result = 0
        for n in name_list:
            if n in dic:
                result += dic[n]
        else:
            answer.append(result)
    return answer