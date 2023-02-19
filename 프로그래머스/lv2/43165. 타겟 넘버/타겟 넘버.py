def solution(numbers, target):
    res = [0]
    def dfs(i, n, l):
        if i == len(l) and n == target:
            res[0] += 1
            return
        elif i == len(l) and n != target:
            return
        
        v = l[i] 
        dfs(i + 1, n + v, l)
        dfs(i + 1, n - v, l)

    dfs(0, 0, numbers)

    return res[0]