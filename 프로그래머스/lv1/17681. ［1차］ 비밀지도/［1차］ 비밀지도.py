def numtosharp(x):
    result = ""
    for i in x:
        if i == '1': result += "#"
        else: result += " "
    return result
def solution(n, arr1, arr2):
    answer = []
    for one, two in zip(arr1, arr2):
        check = bin(one | two)[2:]
        if len(check) < n: check = '0' * (n - len(check)) + check
        answer.append(numtosharp(check))
    return answer