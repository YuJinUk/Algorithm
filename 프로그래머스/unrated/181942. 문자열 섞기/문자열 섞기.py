def solution(str1, str2):
    answer = ''
    l = max(len(str1),len(str2))
    for i in range(l):
        answer += str1[i] + str2[i]
    return answer