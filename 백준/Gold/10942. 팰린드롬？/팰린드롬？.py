from sys import stdin
n = int(stdin.readline())
palindrom = [0] + list(map(int,stdin.readline().split()))
m = int(stdin.readline())
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i]=1

for i in range(n-1,0,-1):
    for j in range(n,i-1,-1):
        if palindrom[i]==palindrom[j]:
            if i+1==j or dp[i+1][j-1]==1:
                dp[i][j]=1

for _ in range(m):
    a, b=map(int,stdin.readline().split())
    print(dp[a][b])