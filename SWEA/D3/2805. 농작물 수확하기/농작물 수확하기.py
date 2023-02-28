T = int(input())
for tt in range(1, T+1):
    n = int(input())
    answer = 0
    column = n//2
    for i in range(n):
        board = list(map(int, list(input())))
        answer += sum(board[column-i:column+i+1]) if i <= column else sum(board[column -(n-1-i) :column + n-i])
    print(f'#{tt} {answer}')