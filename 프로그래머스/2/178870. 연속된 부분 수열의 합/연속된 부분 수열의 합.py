def solution(sequence, k):
    l = len(sequence)
    left, right, check, answer = 0, 0, sequence[0], [0, 1000001]
    if check == k:
        return [0,0]
    for i in range(1, l):
        right = i
        check += sequence[i]
        while check > k:
            check -= sequence[left]
            left += 1
        if check == k:
            if answer[1] - answer [0] > right - left:
                answer[0], answer[1] = left, right
            elif answer[1] - answer [0] == right - left and answer[0] > left:
                answer[0], answer[1] = left, right
    return answer