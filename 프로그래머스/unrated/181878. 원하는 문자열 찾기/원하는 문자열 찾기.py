def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    sl, l = len(myString), len(pat)
    answer = myString.replace(pat, '')
    return 1 if sl > len(answer) else 0