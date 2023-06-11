def solution(strArr):
    return [i.upper() if idx%2 else i.lower() for idx, i in enumerate(strArr)]