a, b, c = map(int, input().split())

def bi(n):
    # print(n)
    if n == 1:
        return a % c
    elif n == 2:
        return (a * a) % c
    check = bi(n//2)
    # print('check', check)
    if n % 2:
        return (check * check * a) % c
    elif not n % 2:
        return (check * check) % c
print(bi(b) % c)