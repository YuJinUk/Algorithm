def solution(seoul):
    idx = [i for i in range(len(seoul)) if seoul[i] == "Kim"]
    return "김서방은 %d에 있다"%(idx[0])