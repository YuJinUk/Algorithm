s = int(input())

star = '*'
space = ' '
def rec(n):
    if n == 1:
        return [star]
    check = rec(n//3)
    # print('check', check)
    # if n <= s:
        # check = check * 4 + ' '*((n//3)**2) + check * 4
    check_2 = []
    for i in check:
        check_2.append(i * 3)
    # print('1',check_2)
    for i in check:
        check_2.append(i + space*(n//3) + i)
    # print('2',check_2)
    for i in check:
        check_2.append(i * 3)
    # print('3',check_2)
    return check_2

c = rec(s)
# print(c)
for i in c:
    print(i)