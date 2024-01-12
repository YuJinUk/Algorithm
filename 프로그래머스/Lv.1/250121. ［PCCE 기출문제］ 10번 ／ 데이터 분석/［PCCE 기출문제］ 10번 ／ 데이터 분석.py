def solution(data, ext, val_ext, sort_by):
    answer = []
    name = ['code', 'date', 'maximum', 'remain']
    idx = name.index(ext)
    sort_idx = name.index(sort_by)
    for lst in data:
        if lst[idx] >= val_ext:
            continue
        answer.append(lst)
    return sorted(answer, key = lambda x: x[sort_idx])