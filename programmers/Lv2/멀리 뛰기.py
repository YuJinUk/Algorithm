def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    li = [1,2] # 1과 2를 만들기 위한 경우의수를 list로 만들어둠
    for i in range(2,n):
        li.append(li[i-2]+li[i-1]) # (i-1)번째에 1을 더하거나 (i-2)번째에 2를 더하여 i번째 경우의 수를 구한다.
    return li[-1]%1234567