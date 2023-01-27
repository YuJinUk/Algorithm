def solution(s):
    first = 0 # (의 개수
    second = 0 # )의 개수
    for i in s:
        if first < second: # 만약 )의 개수가 많아지면 잘못된 괄호가 생성 > return False
            return False
        if i == '(':
            first += 1
        else:
            second += 1
    if first != second: # 만약 개수가 다르면 return False
        return False
    return True