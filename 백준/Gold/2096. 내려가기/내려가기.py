import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input().rstrip())
matrix = []
min_matrix = []

x, y, z = map(int, input().rstrip().split())
matrix, min_matrix = [x, y, z], [x, y, z]

for i in range(1, N):
    x, y, z = map(int, input().rstrip().split())
    minboard, maxboard = [0, 0, 0], [0, 0, 0]
    for idx in range(3):
        if not idx: 
            maxnum = max(matrix[:idx+2])
            minnum = min(min_matrix[:idx+2])
            minboard[idx] = x + minnum
            maxboard[idx] = x + maxnum
        elif idx == 2: 
            maxnum = max(matrix[idx-1:])
            minnum = min(min_matrix[idx-1:])
            minboard[idx] = z + minnum
            maxboard[idx] = z + maxnum
        else:         
            maxnum = max(matrix)
            minnum = min(min_matrix)
            minboard[idx] = y + minnum
            maxboard[idx] = y + maxnum
    min_matrix = deepcopy(minboard)
    matrix = deepcopy(maxboard)

print(max(matrix), min(min_matrix))