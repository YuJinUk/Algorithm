# 초침이 시침/분침과 겹칠 때마다 알람이 울리는 기능
# 알람이 몇 번 울리는지 알고싶음
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 시작시간과 끝시간을 초단위로 변환
    starttime = h1 * 3600 + m1 * 60 + s1
    endtime = h2 * 3600 + m2 * 60 + s2  

    # next기준으로 계산할거니 포함되지 않는 시작시간 00시, 12시 미리 카운팅
    if starttime == 0 * 3600 or starttime == 12 * 3600:
        answer += 1

    while starttime < endtime:
        # 시침 1시간 = 30도 -> 1초에 30/3600도 즉, 1/120도 이동
        # 분침 1분 = 6도 -> 1초에 6/60도 즉, 1/10도 이동
        # 초침 1초 = 6도 -> 1초에 6도 이동 
        hour_angle = starttime / 120 % 360
        minute_angle = starttime / 10 % 360
        second_angle = starttime * 6 % 360

        # 다음 위치가 360도가 아닌 0도로 계산되어 카운팅에 포함되지 않는 경우 방지
        # 이동했을 때 지나쳤거나 같아졌는지를 비교하는 것이므로 현재위치는 해줄 필요없음
        nxt_hour_angle = 360 if (starttime + 1) / 120 % 360 == 0 else (starttime + 1) / 120 % 360
        nxt_minute_angle = 360 if (starttime + 1) / 10 % 360 == 0 else (starttime + 1) / 10 % 360
        nxt_second_angle = 360 if (starttime + 1) * 6 % 360 == 0 else (starttime + 1) * 6 % 360

        if second_angle < hour_angle and nxt_second_angle >= nxt_hour_angle:
            answer += 1
        if second_angle < minute_angle and nxt_second_angle >= nxt_minute_angle:
            answer += 1
        # 시침/분침과 동시에 겹쳤을 때 중복카운팅 제외 
        if nxt_second_angle == nxt_hour_angle and nxt_hour_angle == nxt_minute_angle:
            answer -= 1

        starttime += 1
    
    return answer