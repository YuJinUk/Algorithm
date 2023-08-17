from math import floor

def check(r):
    cnt = r * 4 + 1
    plus = 0
    for i in range(1, r):
        a, b = str((r**2 - i**2) ** (0.5)).split('.')
        a, b = int(a), int(b)
        if not b:
            plus += 4
        cnt += a * 4
    return cnt, plus

def solution(r1, r2):
    x, xplus = check(r2)
    y, yplus = check(r1)
    return x - y + yplus + 4