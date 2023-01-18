def solution(arr, divisor):
    want_list = [i for i in arr if i%divisor == 0]
    if len(want_list) == 0:
        return [-1]
    else :
        return sorted(want_list)