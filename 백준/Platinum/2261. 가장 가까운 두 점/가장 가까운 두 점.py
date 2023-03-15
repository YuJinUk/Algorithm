# 이분탐색인가?
def euclidean(d1, d2):
    return (d1[0] - d2[0])**2 + (d1[1] - d2[1])**2
# x축 기준 비교 -> y축 기준 비교 -> 가능성있는 것을 줄이고 euclidean distance를 계산 후 최솟값 return
def min_distance(start,end):
    if end == start + 1: # 거리가 1이면 euclidean distance를 계산
        return euclidean(dot[start],dot[end])
    elif end == start: # 거리가 0이면 최댓값을 주고 left or right에서 계산된 값과 비교
        return float('inf')
    mid = (start + end)//2 # 이분탐색을 위해 중앙으로 나눔
    min_e = min(min_distance(start, mid), min_distance(mid+1,end)) #recursion error 조심

    poss = [] # 우선 x축을 기준으로 min_e보다 작은 애들만 가능성이 있으므로 저장
    for i in range(start, end+1):
        if (dot[mid][0] - dot[i][0])**2 < min_e:
            poss.append(dot[i])
    # x축을 기준으로 확인했으므로 y축을 기준으로 볼 차례이므로 재정렬
    poss.sort(key=lambda x: x[1])
    for i in range(len(poss)-1):
        for j in range(i+1,len(poss)):
            if (poss[i][1] - poss[j][1])**2 < min_e:
                distance = euclidean(poss[i], poss[j])
                min_e = min_e if min_e < distance else distance
            else: # 만약 하나라도 큰 값이 나오면 가능성이 0이므로 뒤의 index들을 보지않고 넘김
                break
    return min_e
from sys import stdin
n = int(stdin.readline())
dot = [list(map(int,stdin.readline().split())) for i in range(n)]
dot.sort()
print(min_distance(0, n-1))