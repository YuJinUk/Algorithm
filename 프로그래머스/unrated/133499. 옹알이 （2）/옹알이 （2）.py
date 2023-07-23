def solution(babbling):
    answer = 0
    speak = ["aya","ye","woo","ma"]     #가능한 4가지 발음 리스트
    for i in babbling:                  #babbling 문자열 배열만큼 반복
        for v in speak:                 #4가지 발음으로 반복
            if v*2 not in i:            #연속된 같은발음이 없다면
                i=i.replace(v,' ')      #' '으로 발음을 치환
        if i.strip()=='':               #치환 완료된 문자열의 공백을 제거하고 ''와 같다면
            answer+=1                   #발음가능한 단어로 카운팅
    return answer