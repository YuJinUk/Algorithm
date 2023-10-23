def solution(price, money, count):
    answer = -1
    a = 0
    for i in range(1,count+1):
        a += price * i
    if money >= a :
        return 0
    else:
        return a-money