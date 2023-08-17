def check(x):
    while True:
        mok, mod = divmod(x, 2)
        if mod:
            break
        x = mok
    while True:
        mok, mod = divmod(x, 5)
        if mod:
            break
        x = mok
    return x

def solution(a, b):
    x = check(b)
    if a % x:
        return 2
    return 1