N = int(input()) # 수열의 길이
nums = list(map(int, input().split()))
a = 0
b = 0
result = 0
n_list = []

for i in nums: # 작아지는 개수
    if not n_list:
        n_list.append(i)
    elif n_list[-1] >= i: 
        n_list.append(i)
    else :
        if a < len(n_list):
            a = len(n_list)
        n_list = [i]
if a < len(n_list):
    a = len(n_list)
n_list = []
for i in nums: # 커지는 개수
    if not n_list:
        n_list.append(i)
    elif n_list[-1] <= i: 
        n_list.append(i)
    else :
        if b < len(n_list):
            b = len(n_list)
        n_list = [i]

if b < len(n_list):
    b = len(n_list)
print(max(a,b))
