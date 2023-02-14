T = int(input())
for tt in range(1, T+1):
    n, k = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse = True)
    sum_score = sum(score[:k])
    print(f'#{tt} {sum_score}')