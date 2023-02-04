N = int(input())
n = [list(map(int,input().split())) for _ in range(N)]

def findn(idx):
    if idx == 0 : return 5
    elif idx == 1 : return 3
    elif idx == 2 : return 4
    elif idx == 3 : return 1
    elif idx == 4 : return 2
    else : return 0

result = []

for i in range(6):
    bottom_idx = i
    head_idx = findn(bottom_idx)
    summ = max([i for i in range(1,7) if i != n[0][bottom_idx] and i != n[0][head_idx]])
    for j in range(1, N):
        bottom_idx = n[j].index(n[j-1][head_idx])
        head_idx = findn(bottom_idx)
        summ += max([i for i in range(1,7) if i != n[j][bottom_idx] and i != n[j][head_idx]])
    result.append(summ)

print(max(result))