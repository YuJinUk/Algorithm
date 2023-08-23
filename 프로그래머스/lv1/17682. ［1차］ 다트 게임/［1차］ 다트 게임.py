from collections import deque
def solution(dartResult):
    stack, flag = deque(), 0
    for idx, i in enumerate(dartResult):
        if flag: flag = 0; continue
        if i.isdigit():
            if i == '1' and dartResult[idx + 1] == "0":
                stack.append(int(i + "0")); flag = 1
                continue
            stack.append(int(i))
        elif i.isalpha():
            num = stack.pop()
            if i == "S":
                num = num ** 1
            elif i == "D":
                num = num ** 2
            else:
                num = num ** 3
            stack.append(num)
        elif i == "*":
            if len(stack)>1:
                x1 = stack.pop(); x2 = stack.pop()
                stack.append(x2 * 2); stack.append(x1 * 2)
            else:
                stack.append(stack.pop() * 2)
        else:
             stack.append(stack.pop() * (-1))
    return sum(stack)