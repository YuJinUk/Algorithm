def solution(a, b):
    x, y = int(str(a)+str(b)), int(str(b)+str(a))
    return x if x > y else y