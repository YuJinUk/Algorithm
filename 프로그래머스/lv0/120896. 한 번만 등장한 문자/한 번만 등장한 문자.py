def solution(s):
    check = []
    for i in set(list(s)):
        if s.count(i) ==1:
            check.append(i)
    return ''.join(sorted(check))