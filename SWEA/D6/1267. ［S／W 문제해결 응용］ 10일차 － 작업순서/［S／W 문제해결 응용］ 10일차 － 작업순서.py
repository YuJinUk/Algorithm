for tt in range(1, 11):
    v, e = map(int, input().split())
    line = list(map(int, input().split()))
    result = []
    start = []
    end = []
    for i in range(len(line)):
        if not i % 2 :
            start.append(line[i])
        else:
            end.append(line[i])
    start_dic = dict()
    end_dic = dict()
    for i in range(1, v+1):
        start_dic.setdefault(i, [])
        end_dic.setdefault(i, [])
    for i, j in zip(start, end):
        start_dic[i].append(j)
        end_dic[j].append(i)
    while end_dic:
        for i, j in list(end_dic.items()):
            if not j:
                result.append(i)
                for k in start_dic[i]:
                    end_dic[k].remove(i)
                end_dic.pop(i)
    print(f'#{tt}', *result)