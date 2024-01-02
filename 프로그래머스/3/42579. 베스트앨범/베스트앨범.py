def solution(genres, plays):
    dic = dict()
    for i, j in zip(genres, plays):
        dic.setdefault(i,[])
        dic[i].append(j)
    result = []
    sum_genre = []
    for i in dic:
        dic[i] = sorted(dic[i], reverse = True)
        sum_genre.append((sum(dic[i]),i))
        if len(dic[i]) > 2:
            result.append((dic[i][:2], i))
        else:
            result.append((dic[i], i))
    sum_genre.sort(reverse = True)
    ans = []
    for summ, genre in sum_genre:
        for j in result:
            if genre in j:
                ans.append(j[0])
    re_turn = []
    for i in ans:
        for j in i:
            re_turn.append(plays.index(j))
            plays[plays.index(j)] = 0
    return re_turn