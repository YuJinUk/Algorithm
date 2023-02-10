def solution(s):
    s = s.split(' ')
    answer = ''
    s = [int(s[i]) for i in range(len(s))]
    s = sorted(s)
    answer += str(s[0])
    answer += ' '
    answer += str(s[-1])
    return answer