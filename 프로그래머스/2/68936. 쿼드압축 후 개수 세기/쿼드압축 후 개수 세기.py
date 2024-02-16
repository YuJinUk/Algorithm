summ = [0,0]
def sol(ar):
    global summ
    n = len(ar[0]) # 2
    if n == 1: # 길이가 1이면 숫자 1개만 있으므로 summ에 개수 추가
        if ar[0][0] == 1:
            summ[1] += 1
        if ar[0][0] == 0:
            summ[0] += 1
        return

    
    cnt = 0
    for i in ar: # 0의 개수
        cnt += i.count(0)
    if cnt == n ** 2: # 만약 전체가 0이면 return 0 
        summ[0] += 1
        return
    elif cnt == 0: # 만약 전체가 1이면 return 1
        summ[1] += 1
        return
    
    arr_list = [[] for _ in range(4)] # 무조건 4등분되기 때문
    arr_list_copy = [[] for _ in range(4)] # for문을 쓰지 않고 안에 1과 0의 개수를 파악하기 위한 list
    n_ban = n // 2 # 1
    for i in range(n): # 0, 1
        if i < n_ban:
            arr_list[0].append(ar[i][:n_ban]) # ar[0][:1] 1
            arr_list_copy[0] += ar[i][:n_ban]
            arr_list[1].append(ar[i][n_ban:]) # ar[0][1:] 0
            arr_list_copy[1] += ar[i][n_ban:]
        else:
            arr_list[2].append(ar[i][:n_ban]) # ar[1][:1] 0
            arr_list_copy[2] += ar[i][:n_ban]
            arr_list[3].append(ar[i][n_ban:]) # ar[1][1:] 1
            arr_list_copy[3] += ar[i][n_ban:]
            
    for i in range(4):
        if 1 not in arr_list_copy[i] and len(arr_list_copy[i]) > 1: # 만약 길이가 1보다 크고 1이 없다면
            summ[0] += 1
        elif 0 not in arr_list_copy[i] and len(arr_list_copy[i]) > 1: # 만약 길이가 1보다 크고 0이 없다면
            summ[1] += 1
        else:
            sol(arr_list[i]) # 재귀
            
def solution(arr):
    sol(arr)
    return summ