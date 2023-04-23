import sys
input = sys.stdin.readline

for _ in range(int(input())):
    func = list(input())
    func.pop()
    n = int(input())
    nums = list(map(int, input().strip('[]\n').split(','))) if n else list(input().strip('[]'))
    if not n:
        if 'D' in func:
            print('error')
            continue
        else:
            print('[]')
            continue
    cnt_r, cnt_d = func.count('R'), func.count('D')
    if cnt_d > n:
        print('error')
        continue
    elif cnt_d == n:
        print('[]')
        continue
    
    cnt = 0
    for i in range(len(func)):
        check = func[i]
        if check == 'R':
            cnt += 1
        else:
            if not cnt % 2:
                nums.pop(0)
            else:
                nums.pop()
    else:
        if cnt % 2:
            nums.reverse()
    print('[', end = '')
    for i in range(len(nums)):
        print(nums[i], end = '')
        if i != len(nums)-1:
            print(',', end = '')
    print(']')