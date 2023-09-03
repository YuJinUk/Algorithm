import sys
input = sys.stdin.readline

for _ in range(int(input())):
    answer = 0
    ans = input().rstrip().split('X')
    for i in ans:
        if i:
            l = len(i)
            answer += l * (l + 1) // 2
    print(answer)