def f(x, y):
    if y % 2:
        for i in range(len(x)):
            x[i] *= y
    else:
        for j in range(len(x)):
            x[j] += y
    return x
def solution(arr, k):
    return f(arr, k)