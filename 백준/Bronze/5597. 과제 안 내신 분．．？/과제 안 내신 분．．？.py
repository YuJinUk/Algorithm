lst = [0] * 30
for _ in range(28):
    lst[int(input())-1] = 1
for idx, i in enumerate(lst):
    if not i:
        print(idx+1)