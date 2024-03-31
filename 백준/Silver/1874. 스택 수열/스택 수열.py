import sys

input = sys.stdin.readline

stack = []
N = int(input().rstrip())
answer = [int(input().rstrip()) for i in range(N)]
i = 1
result = []
check = True
for a in answer:
    if a >= i:
        for stack_plus in range(i, a + 1):
            stack.append(stack_plus)
            result.append('+')
        i = a + 1
    if a == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        check = False
        print('NO')
        break
if check:
    for i in result:
        print(i)