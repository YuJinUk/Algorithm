import sys
from math import gcd
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
checking = []
s = nums[0]
checking.append(s)
for i in range(1, n):
    nxt = nums[i]
    s = gcd(s, nxt)
    checking.append(s)
    
reverse_checking = []
ss = nums[-1]
reverse_checking.append(ss)
for i in range(n-2, -1, -1):
    nnxt = nums[i]
    ss = gcd(ss, nnxt)
    reverse_checking.append(ss)
    
answer = checking[-1]
check_num = 0
for i in range(n):
    if not i:
        check = reverse_checking[n-2]
    elif i:
        check = gcd(checking[i-1], reverse_checking[n-2-i])
    if check > answer:
        answer = check
        check_num = nums[i]
        
if answer == s:
    print(-1)
else:
    print(answer, check_num)