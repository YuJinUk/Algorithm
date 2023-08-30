def changelocation(x, y, matrix):
    if not matrix[x][y]:
        for i in range(x-1, -1, -1): # 아래에서 위로 0 이 있다면 바꿔주기
            if matrix[i][y]:
                matrix[x][y], matrix[i][y] = matrix[i][y], matrix[x][y]
                break

def checking(x, y, rm, matrix):
    if matrix[x][y] and matrix[x][y] == matrix[x+1][y] == matrix[x][y+1] == matrix[x+1][y+1]:
            rm.add((x,y))
            rm.add((x+1,y))
            rm.add((x,y+1))
            rm.add((x+1,y+1))
            
def solution(m, n, board):
    matrix = [list(x) for x in board]
    while True:
        rm = set()
        
        for x in range(m-1): # height
            for y in range(n-1): # width
                checking(x, y, rm, matrix)

        if not len(rm): # 지워질 박스가 없을 때
            answer = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == 0:
                        answer += 1
            return answer
        
        for i in rm: # 0으로 바꿔주기
            matrix[i[0]][i[1]] = 0

        for x in range(m-1,-1,-1):
            for y in range(n):
                changelocation(x,y,matrix)
    