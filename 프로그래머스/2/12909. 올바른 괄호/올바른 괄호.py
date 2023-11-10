def solution(s):
    first = 0
    second = 0
    for i in s:
        if first < second:
            return False
        if i == '(':
            first += 1
        else:
            second += 1
    if first != second:
        return False
    return True