def solution(bandage, health, attacks):
    # 붕대감기 : 기술 이름

    # t초동안 붕대감음
    # 1초마다 x만큼 체력 회복
    # 붕대감기 성공 -> y만큼 추가체력 회복 but 최대 체력 이상으론 불가능

    # 공격당하는 순간 -> 체력회복 불가능
    # 기술 사용중 공격당함 -> 기술 취소
    # 기술 취소 or 기술 끝 -> 바로 붕대감기 다시 사용 -> 연속 성공시간 0으로 초기화

    # 체력 0되면 사망

    # 죽으면 return -1
    # 살면 끝나고 남은 체력을 return
    
    
    t, x, y = bandage
    l = len(attacks)
    max_health = health
    past_attack_time, past_damage = 0, 0
    for i in range(l):
        attack_time, damage = attacks[i]
        gap_time = attack_time - past_attack_time - 1
        mok, mod = divmod(gap_time, t)
        health += mok * y + gap_time * x
        
        if health > max_health:
            health = max_health
        
        health -= damage
        
        if health <= 0:
            return -1
        
        past_attack_time, past_damage = attack_time, damage
        
    return health













