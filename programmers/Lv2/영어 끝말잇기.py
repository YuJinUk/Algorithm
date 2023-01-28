from collections import deque
def solution(n, words):
    words_list = deque()
    for i in words:
        if len(words_list) == 0:
            words_list.append(i)
        else:
            if words_list[-1][-1] != i[0] or i in words_list:
                people, turn = len(words_list) % n+1, len(words_list)//n+1
                return [people, turn]
            else:
                words_list.append(i)
    return [0,0]