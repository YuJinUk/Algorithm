from collections import defaultdict
def solution(survey, choices):
    dic, check, answer = defaultdict(int), [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"] ], ""
    for x in survey: dic[x[0]]; dic[x[1]]
    for surv, choice in zip(survey, choices):
        if choice < 4: dic[surv[0]] += abs(choice - 4)
        elif choice > 4: dic[surv[1]] += choice - 4
    for lst in check:
        if dic[lst[0]] >= dic[lst[1]]: answer += lst[0]
        else: answer += lst[1]
    return answer