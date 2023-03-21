from sys import stdin
n, k = map(int, stdin.readline().split())
items = sorted([tuple(map(int, stdin.readline().split())) for _ in range(n)])

values, weights= [0]*(k+1), set()

for i in items:
    for j in range(k,i[0]-1,-1):
        values[j] = max(values[j], values[j-i[0]]+i[1])
print(max(values))