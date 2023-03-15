def solution(emergency):
    s = sorted(emergency, reverse = True)
    answer = [0] * len(emergency)
    for idx, i in enumerate(s):
        answer[emergency.index(i)] = idx+1
    return answer