def solution(msg):
    dic = dict()
    for i in range(65, 91):
        dic[chr(i)] = i-64
    answer = []
    l = len(msg)
    i = 0
    s = ''
    while i < l:
        if not s:
            s += msg[i]
            continue
        if s in dic:
            if i < l-1:
                i += 1
                s += msg[i]
            else:
                answer.append(dic[s])
                break
        else:
            dic[s] = len(dic) + 1
            answer.append(dic[s[:-1]])
            s = msg[i]
    return answer