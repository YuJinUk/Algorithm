def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 대문자 -> 소문자
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-','_','.']:
            answer += i
    # while '..' not in answer:
    while True:
        answer = answer.replace('..','.')
        if '..' not in answer:
            break
    answer = answer.lstrip('.')
    answer = answer.rstrip('.')
    if answer == '':
        answer += 'a'
    if len(answer)>= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    if 2 >= len(answer):
        while True:
            aa = answer[-1]
            answer += aa
            if len(answer) == 3:
                break
    return answer