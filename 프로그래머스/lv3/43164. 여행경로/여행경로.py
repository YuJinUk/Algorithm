def solution(tickets):
    dic = dict()
    for ticket in tickets:
        dic.setdefault(ticket[0],[])
        dic[ticket[0]].append(ticket[1])
    for r in dic:
        dic[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(dic[top][-1])
            dic[top] = dic[top][:-1]
    return path[::-1]