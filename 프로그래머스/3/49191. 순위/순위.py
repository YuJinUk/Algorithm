def solution(n, results):
    dic_child = dict()
    dic_parent = dict()
    for i in range(1, n+1):
        dic_child.setdefault(i,[])
        dic_parent.setdefault(i,[])
    for win, lose in results:
        dic_child[win].append(lose)
        dic_parent[lose].append(win)
    result = [0 for _ in range(n+1)]
    for p in range(1, n+1):
        check = [False] * (n+1)
        visit = []
        visit.append(p)
        check[p] = True
        while visit:
            v = visit.pop()
            for k in dic_child[v]:
                if not check[k]:
                    check[k] = True
                    visit.append(k)
                    result[p] += 1
    for p in range(1, n+1):
        check = [False] * (n+1)
        visit = []
        visit.append(p)
        check[p] = True
        while visit:
            v = visit.pop()
            for k in dic_parent[v]:
                if not check[k]:
                    check[k] = True
                    visit.append(k)
                    result[p] += 1
    answer = 0
    for i in result:
        if i == n-1:
            answer += 1
    return answer