def solution(num_list):
    odds, even = '', ''
    for i in num_list: 
        if i%2 : even += str(i)
        else : odds += str(i)
    return int(odds) + int(even)