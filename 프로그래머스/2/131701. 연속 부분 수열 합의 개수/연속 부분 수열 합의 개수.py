def solution(x):
    l = len(x) # 원소의 개수
    new_list = x * 2
    result = []
    for i in range(1,l+1):
        for j in range(l):
            result.append(sum(new_list[j:j+i]))
    return len(set(result))
    