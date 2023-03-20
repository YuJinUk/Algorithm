# heapq로 다시 풀어보기
import heapq
def solution(n,k,enemy):
    result = 0
    enemy_list = []
    sum_enemy = 0
    for i in enemy:
        heapq.heappush(enemy_list,-i)
        sum_enemy += -i
        if -sum_enemy <= n:
            result += 1
        else:
            if k>0:
                a = heapq.heappop(enemy_list)
                sum_enemy -= a
                k -=1
                result += 1
            else :
                return result
                
    return result