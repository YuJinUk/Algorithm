def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    li = [1,2]
    for i in range(2,n):
        li.append(li[i-2]+li[i-1])
    return li[-1]%1234567