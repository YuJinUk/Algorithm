def solution(s, skip, index):
    check = 'abcdefghijklmnopqrstuvwxyz'
    check = list(check)
    for i in skip:
        check.remove(i)
    check = check + check + check
    answer = ''
    for i in s:
        answer += check[check.index(i) + index]
    return answer