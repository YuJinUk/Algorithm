def solution(s):
    s = s.lower()
    plist = [s[i] for i in range(len(s)) if s[i] == 'p']
    ylist = [s[i] for i in range(len(s)) if s[i] == 'y']
    if len(plist) == len(ylist):
        return True
    else:
        return False