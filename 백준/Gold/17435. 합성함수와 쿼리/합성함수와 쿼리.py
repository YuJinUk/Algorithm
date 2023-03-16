from sys import stdin
from math import log2

m = int(stdin.readline())
m_list = list(map(int, stdin.readline().split()))
q = int(stdin.readline())
nx = [list(map(int, stdin.readline().split())) for _ in range(q)]

l = 19 # int(log2(500000)) + 1
b = [[0]*l for _ in range(m+1)]
for i in range(1,m+1):
    b[i][0] = m_list[i-1]
# 예를 들어 1 -> 3 / 3 -> 5이고 i, j = 1, 1 일때
# b[1][1] = b[b[1][0]][0]인데
# b[1][0]은 1에서 가는 위치이므로 3
# b[3][0]은 3에서 가는 위치이므로 5
# 따라서 2^1번 지났을때의 값을 b[1][1]에 저장해주고
# 2^2번 지났을때의 값을 b[1][2]에 저장해준다.
for i in range(1,l):
    for j in range(1,m+1):
        b[j][i] = b[b[j][i-1]][i-1]
        
# 비트의 이동을 통해 만약 n이 그 수보다 크거나 같다면 빼서 최대한 작은수로 바꾼 후 그 x값을 출력한다.
for n, x in nx:
    for i in range(l-1,-1,-1):
        if n >= (1<<i):
            n -= (1<<i)
            x = b[x][i]
            
    print(x)