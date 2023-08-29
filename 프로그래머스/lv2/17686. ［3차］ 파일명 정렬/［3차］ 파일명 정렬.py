def solution(files):
    result = []
    for idx, file in enumerate(files):
        file = file.lower()
        j  = 0
        head, num = "", ""
        for xdx, x in enumerate(file):
            if x.isdigit():
                j += 1
                num += x
            elif not x.isdigit():
                if j:
                    break
                head += x
        result.append([head, int(num), idx])
    result = sorted(result, key = lambda x: (x[0], x[1], x[2]))
    return [files[i[2]] for i in result]
