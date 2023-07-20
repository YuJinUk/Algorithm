def solution(s):
    s = list(s)
    check, answer = "", []
    num = ["0","1","2","3","4","5","6","7","8","9"]
    alpha = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in s:
        check += i
        if check in num:
            check = ""
            answer.append(i)
        elif check in alpha:
            answer.append(num[alpha.index(check)])
            check = ""
    return int(''.join(answer))
