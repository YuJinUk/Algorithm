# union-find algorithm
def solution(n, costs):
    parent = [i for i in range(n+1)]
    costs.sort(key = lambda x: x[2]) # 사이즈가 작은 애들부터 연결시키기 위해
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x,y):
        x = find(x)
        y = find(y)
        if x > y:
            parent[x] = y
        elif x < y:
            parent[y] = x
    
    ans = 0
    for x1, x2, value in costs:
        if find(x1) != find(x2):
            union(x1,x2)
            ans += value
    return ans