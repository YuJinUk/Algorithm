# segment tree 연습 2042 구간 합 구하기
# 1. 트리 만들기
def init(start, end, idx):
	# start와 end가 같다면 리프노드이다.
    if start == end:
        tree[idx] = nums[start-1]
        return tree[idx]
	
    # 현재 노드는 왼쪽 아래 노드와 오른쪽 아래 노드를 더한 값이다.
    mid = (start+end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid+1, end, idx*2+1)
    return tree[idx]

       
# 2. 트리에서 값 찾기
def find(start, end, idx, left, right):
	# 찾으려는 범위가 start~end 범위보다 클 경우
    if start > right or end < left:
        return 0
        
    # 찾으려는 범위가 segment tree 노드안에 구현되어 있을 경우
    if start >= left and end <= right:
        return tree[idx]

	# 코드를 동작시키기 위한 기본 코드
    # 현재 노드는 왼쪽아래 + 오른쪽아래 노드이다.
    mid = (start + end) // 2
    return find(start, mid, idx*2, left, right) + find(mid+1, end, idx*2+1, left, right)


# 3. 트리 값 바꿔주기
def update(start, end, idx, update_idx, update_data):
	# update 하려는 범위가 초과될 경우
    if start > update_idx or end < update_idx:
        return
    
    tree[idx] += update_data
	
    # 리프노드까지 바꿔주었으면 재귀함수를 끝낸다.
    if start == end:
        return

	# 내가 관여하고 있는 노드들을 찾아서 바꿔준다 -> 재귀함수로 구현
    mid = (start + end) // 2
    update(start, mid, idx*2, update_idx, update_data)
    update(mid+1, end, idx*2+1, update_idx, update_data)

from sys import stdin
from math import ceil, log2

n, m, k = map(int,stdin.readline().split())
nums = [int(stdin.readline()) for _ in range(n)]
depth = int(ceil(log2(n)))
cnt_all = 1 << (depth + 1)
tree = [0] * cnt_all

init(1, n, 1)

for _ in range(m+k):
    a, b, c = map(int,stdin.readline().split())
    if a == 1:
        check = c - nums[b-1]
        nums[b-1] = c
        update(1, n, 1, b, check)

    elif a == 2:
        print(find(1, n, 1, b, c))