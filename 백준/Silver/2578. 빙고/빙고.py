def check(index_list):
    ans = 0
    cnt_0 = 0
    cnt_5 = 0
    for idx, i in enumerate(index_list):
        if sum(i) == 5: # 행
            ans += 1
        if sum([j[idx] for j in index_list]) == 5: # 열
            ans += 1
        cnt_0 += i[idx]
        cnt_5 += i[4-idx]
    if cnt_0 == 5:
        ans += 1
    if cnt_5 == 5:
        ans += 1
    return ans

bingo = []
for _ in range(5):
    bingo += list(map(int, input().split()))
nums = []
for _ in range(5):
    nums += list(map(int, input().split()))

idx_list = [[0]*5 for _ in range(5)]

for idx in range(len(nums)):
    idx_in = bingo.index(nums[idx])
    idx_list[idx_in//5][idx_in%5] = 1
    
    if idx > 5:
        answer = check(idx_list)
        if answer >= 3:
            print(idx+1)
            break