def solution(my_string):
    s = 0
    check = ''
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            check += my_string[i]
        elif check != '':
            s += int(check)
            check = ''
    else:
        if check != '':
            s += int(check)
    return s