# 1215_회문
T = 10
for tt in range(1, T+1):
    m = input()
    matrix = [input() for _ in range(8)]
    for i in range(8): # 세로줄 문자 넣기
        columns = []
        for j in range(8):
            columns.append(matrix[j][i])
        matrix.append(''.join(columns))

    new = [alpha[k:k+int(m)] for alpha in matrix for k in range(8-int(m)+1) if alpha[k] == alpha[k+int(m)-1] ]
    cnt = 0
    for c in new:
        c_list = list(c)
        i = int(m)//2
        while i>0:
            left = c_list.pop(0)
            right = c_list.pop()
            if left != right:
                break
            i -= 1
        if i == 0:
            cnt += 1
    print(f'#{tt} {cnt}')