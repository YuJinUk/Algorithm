def solution(cards):
    card_split = [list() for _ in range(len(cards))] # 


    # loop 만드는 함수
    def cardbox(card, box):
        if cards[card-1] in box:
            return box
        else:
            box.append(cards[card-1])
        return cardbox(box[-1], box)
    # cards의 모든 원소에 대하여 만듦
    i = 0
    for j in cards:
        if j in card_split[i]:
            cardbox(j, card_split[i])
            i += 1
        else: 
            cardbox(j, card_split[i])
            i += 1
    

    # 2차원 list를 길이만 추출하여 1차원 list로 수정
    for i in range(len(card_split)):
        card_split[i] = len(card_split[i])
        
    # set을 통해 중복을 제거
    set_card_split = list(set(card_split))

    count_list = [] # 중복된 것을 모두 제거하고 남은 것들의 갯수를 list로 저장

    for i in set_card_split:
        count_i = card_split.count(i) # i가 몇개있는 지 갯수 저장
        count_pair = count_i//i # 나눠주면 i개가 포함된 loop의 갯수를 구할 수 있다.
        for _ in range(count_pair):
            count_list.append(i)
    
    count_list.sort()
    
    # 만약 길이가 1이면 1번상자 그룹을 제외하고 상자가 없는 것이므로 0
    # 나머지는 가장 큰 2개의 값을 곱해주면 최대값이 리턴된다
    if len(count_list) == 1:
        return 0
    else:
        return count_list[-1] * count_list[-2]