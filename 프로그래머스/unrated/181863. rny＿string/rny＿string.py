def solution(rny_string):
    answer = ''
    for i in rny_string:
        answer += i if i != 'm' else 'rn'
    return answer