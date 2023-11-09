def solution(id_list, report, k):
    dic = {}
    check_dic = {}
    answer = [0 for _ in range(len(id_list))]
    idx_list = {n:ndx for ndx, n in enumerate(id_list)}
    report = list(set(report))
    for lst in report:
        x, y = lst.split(' ')
        if y not in dic:
            dic[y] = [x]
        else:
            dic[y].append(x)
        if y not in check_dic:
            check_dic[y] = 1
        else:
            check_dic[y] += 1
    for idx, name in enumerate(id_list):
        if name in check_dic and check_dic[name] >= k:
            check = dic[name]
            for i in check:
                answer[idx_list[i]] += 1
    return answer