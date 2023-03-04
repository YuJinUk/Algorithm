def sosu(n):
    if n == 1:
        return 0
    check = 0
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            check += 1
            break
    return 0 if check else 1 # 소수면 1 아니면 0

def bjin(a, b): # b진법으로 변환
    rev_base = ''

    while a > 0:
        a, mod = divmod(a, b)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n, k):
    new = bjin(n,k)
    div = new.split('0')
    result = 0
    for i in div:
        if i.isdigit() and int(i) > 1:
            result += sosu(int(i))
    return result