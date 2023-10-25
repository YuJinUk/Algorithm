def solution(s):
    if s.isdigit():
        if len(s) == 4:
            return True
        elif len(s) == 6:
            return True
        else:
            return False
    else:
        return False