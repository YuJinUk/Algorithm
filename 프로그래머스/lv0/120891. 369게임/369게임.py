def solution(order):
    return len([i for i in str(order) if not int(i)%3 and int(i)])