# segment tree
# 백준 10868 최솟값
from math import log2, ceil
from sys import stdin

n, m = map(int, stdin.readline().split())
nums = [int(stdin.readline()) for _ in range(n)]

depth = int(ceil(log2(n)))
cnt_all = 1 << (depth + 1)
tree = [0] * cnt_all

# 이분 탐색느낌
# start, end는 시작점과 끝점으로 mid값을 기준으로 좌우 방향으로 갱신해준다.
# left, right는 찾고싶은 범위
# segment tree 초기화 시키기
def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init(node*2, start, mid), init(node*2 + 1, mid+1, end))
    return tree[node]

# 만약 start보다 right가 작거나 end보다 left가 큰 경우가 있다면 예외처리해준다.
# left와 right 사이에 start와 end가 있다면 그 떄의 node값이 최소값이 된다.
# 나머지는 확실한 상황이 나올때까지 재귀를 통해 최소값을 구해간다.
def find(node, start, end, left, right):
    if right < start or end < left:
        return int(1e9)
    elif left <= start <= end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(find(2*node, start, mid, left, right), find(2*node + 1, mid + 1, end, left, right))

init(1, 0, n-1) # 시작노드를 1로두고 start = 0, end = n-1로 시작하여 트리를 만들기
# 트리를 만들었으면 m개의 데이터를 받아와서 segment tree를 통해 빠르게 m * logn의 시간복잡도로 구함
for _ in range(m):
    left, right = map(int, stdin.readline().split())
    answer = find(1, 0, n-1, left-1, right-1)
    print(answer)