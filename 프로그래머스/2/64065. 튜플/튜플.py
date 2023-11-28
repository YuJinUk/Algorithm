def solution(s):
    s = list(s.split('}'))
    stack = []
    for i in s:
        if not i:
            continue
        i = i.strip(',{')
        stack.append(i)
    check = []
    for j in stack:
        check.append(j.split(','))
    check.sort(key = lambda x : len(x))
    answer = []
    for i in check:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer