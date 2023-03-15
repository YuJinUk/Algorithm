def solution(array, n):
    check, check_num = float('inf'), 0
    if n in array:
        return n
    array.sort()
    for i in array:
        if check > abs(i - n):
            check = abs(i - n)
            check_num = i
    return check_num