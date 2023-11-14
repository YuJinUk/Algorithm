def solution(n, left, right):
    li = []
    left_quo, left_rem = left // n, left % n
    right_quo, right_rem = right // n, right % n
    for i in range(left_quo+1,right_quo+2):
        for _ in range(i):
            li.append(i)
        for j in range(i+1, n+1):
            li.append(j)
    return li[left_rem:(right_quo-left_quo)*n+right_rem+1]