def solution(s):
    s = s.lower()
    s = s.split(" ")
    new = []
    for i in range(len(s)):
        if len(s[i]) ==1:
            new.append(s[i][0].upper())
        elif len(s[i]) ==0:
            new.append(s[i])
        else:
            new.append(s[i][0].upper() + s[i][1:])
    return " ".join(new)