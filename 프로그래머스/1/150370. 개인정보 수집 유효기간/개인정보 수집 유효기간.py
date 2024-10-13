from collections import defaultdict

def sum_func(y, m, d, t):
    if d == 1:
        d = 28
        m += t - 1
        while m > 12:
            y += 1; m -= 12
    else:
        d -= 1; m += t;
        while m > 12:
            y += 1; m -= 12
    
    return y, m, d

def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = [int(i) for i in today.split(".")]
    dic_term = defaultdict(list)
    
    for i in terms:
        person, term = i.split(" ")
        dic_term[person].append(int(term))
    
    dic_privacy = defaultdict(list)
    for idx, i in enumerate(privacies):
        idx += 1
        start, person = i.split(" ")
        y, m, d = start.split(".")
        y, m, d = int(y), int(m), int(d)
        t = dic_term[person][0]
        y, m, d = sum_func(y, m, d, t)
        
        if y < today_y:
            answer.append(idx)
        elif y == today_y:
            if m < today_m:
                answer.append(idx)
                continue
            elif m == today_m:
                if d < today_d:
                    answer.append(idx)
            
    
    return answer