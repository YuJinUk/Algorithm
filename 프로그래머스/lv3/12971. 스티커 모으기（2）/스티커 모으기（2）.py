def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker)
    
    dp1, dp2 = [0]*len(sticker), [0]*len(sticker)
    dp1[0], dp1[1] = sticker[0], sticker[0] # 첫 번째 원소를 선택하면 두 번째 원소를 선택 못하기 때문에 최댓값을 위해 1번 index에 첫 번째 원소의 값을 지정해주어 다음 스티커를 뽑을 때 지장이 없도록 함
    dp2[1] = sticker[1] # 두 번째 원소를 뽑을 때 첫 번째 원소를 뽑지 못하기 때문에 첫 번째 원소를 0으로 두어 지장이 없도록 함
    
    for i in range(2,len(sticker)-1): # 첫 번째 원소를 선택하면 마지막 원소를 선택 못함
        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])
        
    for j in range(2,len(sticker)): # 두 번째 원소를 선택하면 첫 번째 원소를 선택 못함
        dp2[j] = max(dp2[j-2]+sticker[j], dp2[j-1])
    return max(dp1[-2], dp2[-1])
