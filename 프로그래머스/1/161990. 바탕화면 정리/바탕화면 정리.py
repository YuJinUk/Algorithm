def solution(wallpaper):
    sharp = []
    max_x, min_x, max_y, min_y = 0, 10**3, 0, 10**3
    for rowidx, row in enumerate(wallpaper):
        for idx, i in enumerate(row):
            if i == '#':
                sharp.append((rowidx, idx))
                if rowidx > max_x:
                    max_x = rowidx
                if rowidx < min_x:
                    min_x = rowidx
                if idx > max_y:
                    max_y = idx
                if idx < min_y:
                    min_y = idx
    return [min_x, min_y, max_x+1, max_y+1]