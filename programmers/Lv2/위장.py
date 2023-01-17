def solution(clo):
    answer = 1
    type = []
    for i in range(len(clo)):
        type.append(clo[i][1]) # 의상의 타입만 가져오기
    type = sorted(type) # 같은 종류의 의상끼리 나열될 수 있게 sorted를 취해줌
    # li는 i번째와 (i+1)번째의 옷의 종류가 다르다면 (i+1)을 리스트에 저장하고 1개씩만 고를 수 있으므로 len(type)을 리스트에 저장하여 추가해줌
    li = [i+1 for i in range(len(type)-1) if type[i] != type[i+1]]+[len(type)] 
    zz = [li[0]]
    for i in range(len(li)-1):
        zz.append(li[i+1]-li[i])
    for i in range(len(zz)):
        answer = answer *(1+zz[i])
        
    return answer-1