from collections import Counter
def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    check1, check2 = [], []
    for idx in range(len(str1)-1):
        alpha = str1[idx]+str1[idx+1]
        if alpha.isalpha():
            check1.append(alpha)

    for idx in range(len(str2)-1):
        alpha = str2[idx]+str2[idx+1]
        if alpha.isalpha():
            check2.append(alpha)
    cnt1 = Counter(check1)
    cnt2 = Counter(check2)
    minus,plus = 0, 0
    visit = []
    for i in cnt1:
        if i not in visit:
            if i in cnt2:
                minus += min(cnt1[i],cnt2[i])
                plus += max(cnt1[i],cnt2[i])
            else:
                plus += cnt1[i]
            visit.append(i)
    for i in cnt2:
        if i not in visit:
            if i in cnt1:
                minus += min(cnt1[i],cnt2[i])
                plus += max(cnt1[i],cnt2[i])
            else:
                plus += cnt2[i]
            visit.append(i)
    if plus:
        return int(65536 * minus/plus)
    elif plus == 0:
        return 65536