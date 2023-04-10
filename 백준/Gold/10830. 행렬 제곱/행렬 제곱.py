def matrixmult(A,B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j] % 1000
    return C

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
c = 1000
def bi(n):
    # print(n)
    if n == 1:
        return matrix
    elif n == 2:
        return matrixmult(matrix, matrix)
    check = bi(n//2)
    # print('check', check)
    if n % 2:
        return matrixmult(matrixmult(check, check), matrix)
    elif not n % 2:
        return matrixmult(check, check)
answer = bi(b)
for i in answer:
    for j in i:
        print(j % 1000, end = ' ')
    print()