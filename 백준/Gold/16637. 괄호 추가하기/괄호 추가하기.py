import sys
input = sys.stdin.readline

N = int(input())
cal = list(input().rstrip())
answer = float('-inf')

def dfs(i, value):
    global answer
    if N == i:
        if int(value) > answer:
            answer = int(value)
        return
    if i+4 <= N:
        dfs(i+4, str(eval(''.join([value, cal[i]] + [str(eval(''.join(cal[i+1:i+4])))]))))
    if i+2 <= N:
        dfs(i+2, str(eval(''.join([value] + cal[i:i+2]))))

dfs(1, cal[0])
print(answer)