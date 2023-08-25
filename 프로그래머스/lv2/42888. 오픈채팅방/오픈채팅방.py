def solution(record):
    answer, name = [], {}
    for txt in record:
        txt = txt.split(" ")
        if txt[1] not in name : name[txt[1]] = txt[2]
        if txt[0] == "Enter":
            answer.append((1, txt[1]))
            name[txt[1]] = txt[2]
        elif txt[0] == "Leave":
            answer.append((0, txt[1]))
        elif txt[0] == "Change":
            name[txt[1]] = txt[2]
    result = []
    for x, y in answer:
        if x: result.append(f'{name[y]}님이 들어왔습니다.')
        else: result.append(f'{name[y]}님이 나갔습니다.')
    return result