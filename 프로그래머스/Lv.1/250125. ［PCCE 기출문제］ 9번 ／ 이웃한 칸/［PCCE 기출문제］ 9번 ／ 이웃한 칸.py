def solution(board, h, w):
    answer = 0
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dx, dy in dxdy:
        nx, ny = h + dx, w + dy
        if -1 < nx < len(board) and -1 < ny < len(board[0]):
            if board[nx][ny] == board[h][w]:
                answer += 1
    return answer