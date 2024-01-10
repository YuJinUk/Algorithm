def solution(friends, gifts):
    answer = 0
    
    '''
    이전에 선물을 적게 준 사람이
    선물을 줘야함
    '''
    
    '''
    하지만
    주고받은게 하나도 없거나 같다면
    선물지수가 더 큰 사람이 선물을 받음
    ''' 
    
    '''
    선물지수란?
    준 선물 개수 - 받은 선물 개수
    '''
    
    '''
    선물지수까지 같다면 선물을 주고받지 않음
    '''
    
    '''
    friends : 사람 이름 list
    gifts[0] = A B : A가 B에게 선물을 줌
    '''
    
    give, take = {}, {}
    result = {}
    for name in friends:
        give[name] = {}
        take[name] = {}
        result[name] = 0
        
        
    for give_take in gifts:
        g, t = give_take.split(" ")
        if t in give[g]: give[g][t] += 1
        else: give[g][t] = 1
        if g in take[t]: take[t][g] += 1
        else: take[t][g] = 1
    
    gift_point = {}
    for name in friends:
        gift_point[name] = sum(give[name].values()) - sum(take[name].values())
    
    
    for idx, name_1 in enumerate(friends):
        for name_2 in friends[idx+1:]:
            if name_2 in give[name_1]: name_1_to_name_2 = give[name_1][name_2] # name1이 name2한테 준 개수
            else: name_1_to_name_2 = 0
            if name_2 in take[name_1]: name_2_to_name_1 = take[name_1][name_2] # name1이 name2한테 받은 개수
            else: name_2_to_name_1 = 0
            
            if name_1_to_name_2 == name_2_to_name_1: # 만약 주고 받은게 없다거나 같다면 선물지수로 확인
                name_1_point = gift_point[name_1]
                name_2_point = gift_point[name_2]
                if name_1_point == name_2_point: # 만약 포인트까지 같으면 주고받지 않음
                    continue
                elif name_1_point > name_2_point: # name1이 선물지수가 더 크기 떄문에 받아야함
                    result[name_1] += 1
                else: # name2가 더 크면 name2가 받아야함
                    result[name_2] += 1
            
            elif name_1_to_name_2 > name_2_to_name_1: #주고받은게 있는데 name_1가 준게 더 많다면
                result[name_1] += 1
            else:
                result[name_2] += 1
    answer = max(result.values())
    return answer