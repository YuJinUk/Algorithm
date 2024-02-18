def solution(n): # 3진법
    rev_base = ''

    while n > 0:
        n, mod = divmod(n-1, 3) # n-1을 통해 나머지를 0이 아닌 수로 변환
        if mod == 0:
            rev_base += str(1) #나머지를 변환하여 붙여준다.
        elif mod == 1:
            rev_base += str(2)
        else:
            rev_base += str(4)
    return rev_base[::-1] # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력