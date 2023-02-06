def solution(rows, columns, queries):
    dxdy = [(0,1),(1,0),(0,-1),(-1,0)] # 우 / 하 / 좌 / 상
    board = [[0]* columns for _ in range(rows)] # board 만들기
    num = 0
    for x in range(rows):
        for y in range(columns):
            num += 1
            board[x][y] += num
    
    result = []
    for x1,y1,x2,y2 in queries:
        #시작은 왼쪽 줄
        min_num = []
        tmp1 = board[x1-1][y1-1] # 가장 위에 있는 값을 tmp1에 저장해서 오른쪽으로 내려갈 때 이용
        min_num.append(tmp1)
        for i in range(x1, x2): # 위로
            min_num.append(board[i-1][y1-1])
            board[i-1][y1-1] = board[i][y1-1] # [2][1] > [1][1] / [3][1] > [2][1] / [4][1] > [3][1]
        
        tmp2 = board[x1-1][y2-1] # 가장 오른쪽에 있는 값을 tmp2에 저장해서 아래로 내려갈 때 이용
        min_num.append(tmp2)
        for i in range(y2-1, y1-1, -1): # 오른쪽으로 [1][1] > [1][2] / [1][2] > [1][3] / [1][3]은 따로 저장 
            min_num.append(board[x1-1][i])
            board[x1-1][i] = board[x1-1][i-1]
        board[x1-1][y1] = tmp1

        tmp1 = board[x2-1][y2-1]
        min_num.append(tmp1)
        for i in range(x2-1, x1-1, -1): # 아래로
            min_num.append(board[i][y2-1])
            board[i][y2-1] = board[i-1][y2-1]
        board[x1][y2-1] = tmp2

        for i in range(y1, y2): # 왼쪽으로
            min_num.append(board[x2-1][i-1])
            board[x2-1][i-1] = board[x2-1][i]
        board[x2-1][y2-2] = tmp1
        result.append(min(min_num))
    return result