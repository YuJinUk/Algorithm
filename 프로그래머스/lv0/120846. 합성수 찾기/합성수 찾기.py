def sosu(k):
    lst = [1 for i in range(k+1)]
    for i in range(2, k+1):
        for j in range(i, k+1, i):
            lst[j] += 1
    return lst
def solution(n):
    return n - sosu(n).count(2) - 1