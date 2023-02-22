def solution(tickets):
    routes = dict()
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]
# from collections import deque
# def solution(tickets):
#     dic = dict()
#     for ticket in tickets:
#         dic.setdefault(ticket[0],[])
#         dic[ticket[0]].append(ticket[1])
#     start_p = 'ICN'
#     ans = deque()
#     visited = deque()
#     visited.append(start_p)
#     while visited:
#         next_p = visited.pop()
#         for i in next_p:
#             if i not in visited:
#                 visited.append(i)
#         break
#     return dic
