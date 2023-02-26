def solution(lines):
    stack = []
    cnt = 0
    for start, end in lines:
        while start != end:
            if start not in stack:
                stack.append(start)
            else:
                stack.remove(start)
                cnt += 1
            start += 1
    return cnt