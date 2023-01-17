def solution(p):

    p.sort() # 번호의 크기 순으로 배열
    for i in range(len(p)-1): 
        if p[i] == (p[i+1])[:len(p[i])] :  # 작은 숫자부터 [:len(p[i])]로 앞쪽을 잘라주고 접두사인지 비교
            return False

    return True