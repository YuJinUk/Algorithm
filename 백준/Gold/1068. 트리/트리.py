import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
tree = list(map(int, input().split()))
rm_num = int(input())

if tree[rm_num]==-1 :
    print(0)
    sys.exit(0)
    
dic = {i : [] for i in range(n)}

for idx, i in enumerate(tree):
    if i == -1:
        continue
    dic[i].append(idx)

queue = deque()
queue.append(rm_num)
if tree[rm_num] != -1:
    dic[tree[rm_num]].remove(rm_num)
while queue:
    x = queue.popleft()
    for i in dic[x]:
        queue.append(i)
    else:
        dic.pop(x)
        
answer = 0
for i in dic.values():
    if not i:
        answer += 1
print(answer)