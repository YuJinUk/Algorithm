def solution():
    check = []
    for i in range(1, 10001):
        n = i + sum(list(map(int,list(str(i)))))
        if n <= 10000:
            check.append(n)
    for i in range(1, 10001):
        if i not in check:
            print(i)
    return
solution()