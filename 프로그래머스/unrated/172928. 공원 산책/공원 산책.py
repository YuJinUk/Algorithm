from collections import deque
def solution(park, routes):
    matrix = deque()
    nope_row = [[] for _ in range(len(park))]
    nope_col = [[] for _ in range(len(park[0]))]
    row, col = len(park), len(park[0])
    for idx, i in enumerate(park):
        for jdx, j in enumerate(i):
            if j == 'S':
                start = [idx, jdx]
            elif j == 'X':
                nope_row[idx].append(jdx)
                nope_col[jdx].append(idx)
        matrix.append(list(i))
    for i in routes:
        direction, scalar = i.split()
        if direction == 'E':
            nxt = int(scalar)
            if not -1 < start[1] + nxt < col:
                continue
            for k in range(start[1], start[1] + nxt + 1):
                if k in nope_row[start[0]]:
                    break
            else:
                start[1] += nxt
        elif direction == 'S':
            nxt = int(scalar)
            if not -1 < start[0] + nxt < row:
                continue
            for k in range(start[0], start[0] + nxt + 1):
                if k in nope_col[start[1]]:
                    break
            else:
                start[0] += nxt
        elif direction == 'W':
            nxt = int(scalar) * (-1)
            if not -1 < start[1] + nxt < col:
                continue
            for k in range(start[1] + nxt, start[1] + 1):
                if k in nope_row[start[0]]:
                    break
            else:
                start[1] += nxt
        else:
            nxt = int(scalar) * (-1)
            if not -1 < start[0] + nxt < row:
                continue
            for k in range(start[0] + nxt, start[0] + 1):
                if k in nope_col[start[1]]:
                    break
            else:
                start[0] += nxt
    return start