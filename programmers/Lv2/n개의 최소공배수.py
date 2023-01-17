def ls(a,b): # 최대공약수 구하는 def
    min_num = min(a,b)
    max_num = max(a,b)
    li = []
    for i in range(1,min_num+1):
        if min_num%i == 0:
            if max_num%i == 0:
                li.append(i)
    return li[-1]
def solution(arr): # a,b의 최소공배수 == a * b / 최대공약수를 적용하여 최소공배수를 구해주는 def / 또한 a,b의 최소공배수와 c의 최소공배수는 a,b,c의 최소공배수임을 적용
    result = [0]
    result.append(arr[0]*arr[1]//ls(arr[0],arr[1]))
    for i in range(2,len(arr)):
        result.append(result[i-1]*arr[i]//ls(result[i-1],arr[i]))
    return result[-1]