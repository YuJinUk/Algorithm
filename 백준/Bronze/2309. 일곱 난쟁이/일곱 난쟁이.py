from itertools import combinations
n = [int(input()) for _ in range(9)]

n.sort()
remove_list = list(combinations([0,1,2,3,4,5,6,7,8],2))
sum_n = sum(n)

while True:
    remove_position = remove_list.pop()
    first = n[remove_position[0]]
    second = n[remove_position[1]]
    if sum_n - first - second == 100:
        n.remove(first)
        n.remove(second)
        break
for i in range(7):
    print(n[i])