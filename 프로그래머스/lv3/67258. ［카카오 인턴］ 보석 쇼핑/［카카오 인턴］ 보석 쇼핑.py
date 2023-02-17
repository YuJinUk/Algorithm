from collections import deque
def solution(gems):
    gems = deque(gems)
    leng = len(gems)+1
    name_gems = list(set(gems))

    if len(set(gems)) == 1:
        return [1,1]

    check_dic = dict()
    check_queue = deque()

    result = deque()
    rm_list = deque()
    i = 0 # left
    while i < len(gems):
        if leng == len(name_gems):
            break

        check_queue.append(gems[i])
        if gems[i] in check_dic:
            check_dic[gems[i]] += 1
        else:
            check_dic[gems[i]] = 1
        
        if len(check_dic) == len(name_gems):
            l = len(rm_list)
            for j in range(len(check_queue)):
                if len(check_dic) != len(name_gems):
                    break
                if sum(check_dic.values()) < leng:
                    leng = sum(check_dic.values())
                    result.append([l+j+1,i+1])
                rm = check_queue.popleft()
                rm_list.append(rm)
                check_dic[rm] -= 1
                if not check_dic[rm]:
                    check_dic.pop(rm)
        i += 1
    result = sorted(result,key = lambda x: ((x[1]-x[0]),x[0]))
    return result[0]