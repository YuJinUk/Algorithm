# 별 4 동그라미 3 네모 2 세모 1 순으로 힘이 셈 비교하면됨
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_num = a[0]
    b_num = b[0]
    a = a[1:]
    b = b[1:]
    a.sort(reverse=True)
    b.sort(reverse=True)

    for i, j in zip(a,b):
        if i == j:
            continue
        else:
            if i>j:
                print('A')
                break
            else:
                print('B')
                break
    else :
        if a_num == b_num: print('D')
        elif a_num > b_num: print('A')
        else : print('B')