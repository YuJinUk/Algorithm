from sys import stdin
n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
table = [[0]*n for _ in range(n)]

for i in range(n):
    table[i][i] = 1
    
for i in range(n-1):
    if nums[i] == nums[i+1]:
        table[i][i+1] = 1
        
for cnt in range(n-2):
    for i in range(n-2-cnt):
        j = i+2+cnt
        if nums[i]==nums[j] and table[i+1][j-1] == 1:
            table[i][j]=1
# print(table)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    print(table[a-1][b-1])