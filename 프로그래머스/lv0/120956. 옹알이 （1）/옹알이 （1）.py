def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = 0
    for babble in babbling:
        for i in can:
            if i in babble:
                babble = babble.replace(i, ".")
        if babble == "." * len(babble):
            answer += 1
    return answer