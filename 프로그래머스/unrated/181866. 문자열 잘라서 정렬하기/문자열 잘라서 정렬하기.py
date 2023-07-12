def solution(myString):
    answer = sorted(myString.split('x'))
    print(answer)
    while answer[0] == "":
        answer = answer[1:]
    return answer