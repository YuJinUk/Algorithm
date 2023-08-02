def solution(keymap, targets):
    dic, answer = {}, []
    for keylist in keymap:
        for idx, i in enumerate(keylist):
            if i not in dic:
                dic[i] = idx + 1
            else:
                if dic[i] > idx + 1:
                    dic[i] = idx + 1
    print(dic)
    for want_key in targets:
        result = 0
        for i in want_key:
            if i in dic:
                result += dic[i]
            else: 
                answer.append(-1)
                break
        else: 
            answer.append(result)
    return answer