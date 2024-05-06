import sys
input = sys.stdin.readline

N = list(input().rstrip())

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    left, quick, right, cnt = [], lst[len(lst)//2], [], 0
    
    for i in lst:
        if i < quick:
            right.append(i)
        elif i > quick:
            left.append(i)
        else:
            cnt += 1
    
    return quick_sort(left) + [quick] * cnt + quick_sort(right)

result = quick_sort(N)

print(''.join(result))