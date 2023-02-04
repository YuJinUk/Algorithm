n = int(input())
num = list(map(int, input().split()))
result = [1]
for i in range(1,n):
    result.insert(i-num[i],i+1)
print(*result)