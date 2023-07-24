import sys
 
input = sys.stdin.readline
 
n = int(input())
str1 = str(input().strip())
 
dic = {}
result = [0, 0]
start = 0
end = 0
 
while start < len(str1) and end < len(str1):
    
    if str1[end] not in dic:
        dic[str1[end]] = 1
    else:
        dic[str1[end]] += 1

    if len(dic) > n:
        while start <= end and len(dic) > n:
            if dic[str1[start]] == 1:
                dic.pop(str1[start])
            else:
                dic[str1[start]] -= 1
            start += 1
            
    if len(dic) <= n:
        if result[1] - result[0] < end - start:
            result[0] = start
            result[1] = end
            
    end += 1

print(result[1] - result[0] + 1)