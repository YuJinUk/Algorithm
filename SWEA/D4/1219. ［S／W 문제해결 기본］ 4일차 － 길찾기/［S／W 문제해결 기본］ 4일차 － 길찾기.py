for tt in range(1, 11):
    t, n = map(int, input().split())
    node = list(map(int, input().split()))
    start_node = dict()
    start = []
    end = []
    for i in range(len(node)):
        if not i % 2:
            start.append(node[i])
        if i % 2:
            end.append(node[i])
        start_node.setdefault(node[i],[])
    for i, j in zip(start, end):
        start_node[i].append(j)
    s = 0
    visited = []
    visited.append(s)
    result = [False] * 100
    while visited:
        p = visited.pop()
        if p == 99:
            result[99] = True
            break
        if not result[p]:
            result[p] = True
            for i in start_node[p]:
                visited.append(i)
    if result[99]:
        print(f'#{tt} 1')
    else:
        print(f'#{tt} 0')