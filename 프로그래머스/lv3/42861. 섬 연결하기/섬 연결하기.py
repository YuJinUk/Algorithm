# union-find algorithm
def solution(n, costs):
    parent = [i for i in range(n+1)]
    costs.sort(key = lambda x: x[2]) # 사이즈가 작은 애들부터 연결시키기 위해
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x]) # 가장 높은 parent를 찾기 위해 재귀를 돌림
        return parent[x]
    
    def union(x,y):
        x = find(x) # 가장 높은 parent를 찾는 과정
        y = find(y) # 가장 높은 parent를 찾는 과정
        if x > y: # 만약 x가 y보다 크다면 y가 parent, x가 child
            parent[x] = y
        elif x < y:
            parent[y] = x
    
    ans = 0
    for x1, x2, value in costs:
        if find(x1) != find(x2): # x1과 x2가 같다면 자기자신으로 돌아가는 것이므로 value가 증가하기때문에 제외하기 위함
            union(x1,x2)
            ans += value
    return ans