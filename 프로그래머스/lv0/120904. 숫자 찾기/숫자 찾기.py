def solution(num, k):
    try : 
        result = str(num).index(str(k)) + 1
        return result
    except ValueError : 
        return -1