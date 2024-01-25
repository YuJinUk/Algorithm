def ls(a,b):
    min_num = min(a,b)
    max_num = max(a,b)
    li = []
    for i in range(1,min_num+1):
        if min_num%i == 0:
            if max_num%i == 0:
                li.append(i)
    return li[-1]
def solution(arr):
    result = [0]
    result.append(arr[0]*arr[1]//ls(arr[0],arr[1]))
    for i in range(2,len(arr)):
        result.append(result[i-1]*arr[i]//ls(result[i-1],arr[i]))
    return result[-1]