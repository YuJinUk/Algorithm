def check(x, string):
    if string == 'w':
        x += 1
    elif string == 's':
        x -= 1
    elif string == 'd':
        x += 10
    else:
        x -= 10
    return x

def solution(n, control):
    for i in control:
        n = check(n, i)
    return n
        