import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    N_nums = sorted(list(map(int, input().split())))
    M_nums = sorted(list(map(int, input().split())))
    i, j, answer = 0, 0, 0
    while i < N:
        if j == M:
            answer += (N-i-1) * M
            break
        if N_nums[i] > M_nums[j]:
            answer += 1
            j += 1
        elif N_nums[i] <= M_nums[j]:
            i += 1
            if i != N:
                answer += j
    print(answer)