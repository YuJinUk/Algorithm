def solution(players, callings):
    check, check_name = {}, {}
    for idx, i in enumerate(players):
        check[i] = idx
        check_name[idx] = i
    for j in callings:
        plus_idx = check[j]
        check[check_name[plus_idx-1]] += 1
        check[j] -= 1
        check_name[plus_idx] = check_name[plus_idx-1]
        check_name[plus_idx - 1] = j
    l = len(players)
    answer = [0 for _ in range(l)]
    for i in check:
        answer[check[i]] = i
    return answer