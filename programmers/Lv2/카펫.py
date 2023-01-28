def solution(brown, yellow):
    brown = (brown + 4) // 2
    for row in range(brown, 1, -1):
        column = brown - row
        if (row-2)*(column-2) == yellow:
            return [row,column]