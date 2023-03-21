def solution(n):
    answer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if n < 10:
        return answer[n]

    i = 1
    while len(answer) < n + 1:
        if len(answer) <= i:
            return -1
        for nxt in range(0, int(answer[i][-1])):
            desc = answer[i] + answer[nxt]
            answer.append(answer[i] + answer[nxt])
            if len(answer) == n + 1:
                return answer[-1]
        i += 1
        # print(answer)
    return answer[-1]
print(solution(int(input())))