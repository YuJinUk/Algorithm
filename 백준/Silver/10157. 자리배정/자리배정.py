def ticket():
    m, n = map(int, input().split())
    num = int(input())

    if n * m < num :
        return [0]
    i = 0
    j = 1
    while True:
        num -= n-i
        if num <=0:
            if i % 2==0:
                x = i//2 + 1
                y = i//2 + n-i + num
                break
            else:
                x = m - i//2
                y = i//2 + - num + 1
                break
        else :
            i += 1
        num -= m-j
        if num <=0:
            if j % 2==1:
                y = n - j//2
                x = (j+1)//2 + m-j + num
                break
            else:
                y = j//2
                x = j//2 - num + 1
                break
        else:
            j += 1

    return [x, y]

result = ticket()
print(*result)