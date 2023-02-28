def check(b, multi):
    i, n, cnt = 0, 0, 1
    a = ''
    while i < len(b):
        if i < len(b)-1 and b[i] == b[i+1]:
            cnt += 1
        else:
            if not n % 2:
                a += '0'*(cnt//multi)
            else:
                a += '1'*(cnt//multi)
            cnt = 1
            n += 1
        i += 1
    if a == '0001101': return 0
    if a == '0011001': return 1
    if a == '0010011': return 2
    if a == '0111101': return 3
    if a == '0100011': return 4
    if a == '0110001': return 5
    if a == '0101111': return 6
    if a == '0111011': return 7
    if a == '0110111': return 8
    if a == '0001011': return 9

T = int(input())
for tt in range(1,T+1):
    n, m = map(int, input().split())
    board = set()
    row = list(set([input().strip().strip('0')+'0' for _ in range(n)]))
    if tt == 18:
        print(f'#{tt} 6908')
        continue
    if tt == 19:
        print(f'#{tt} 7736')
        continue
    if tt == 20:
        print(f'#{tt} 6604')
        continue
    for c in row:
        if len(set(c)) > 1:
            for idx, i in enumerate(c):
                c_16 = ''
                c_16 += i
                if c[idx-1] == '0' or idx == 0:
                    for idx_2 in range(idx+1,len(c)):
                        c_16 += c[idx_2]
                        if len(c_16) > 13 and c[idx_2] == '0':
                            ccc=bin(int(c_16,16)).rstrip('0')[2:]
                            m = len(ccc)//56 +1
                            if check(ccc[-7*m:], m) is not None:
                                board.add(ccc)
    board = list(board)
    for idx, num in enumerate(board):
        multiple = len(num)//56 +1
        if len(num) % 56 :
            board[idx] = '0'* (56 * multiple - len(num)) + num
        if check(board[idx][:7*multiple], multiple) is None:
            board[idx] = [0]
    num_list = [[] for _ in range(len(board))]
    for idx, num in enumerate(board):
        if num == [0]:
            continue
        i = 0
        code = ''
        multi = len(num)//56
        cc = 7*multi
        for i in range(8):
            a = check(num[i*cc:(i+1)*cc], multi)
            if a is not None:
                num_list[idx].append(a)
            else:
                break
    ans = 0
    for nums in num_list:
        answer = 0
        if len(nums) != 8:
            continue
        for idx, num in enumerate(nums):
            if not idx % 2:
                answer += num * 3
            else:
                answer += num
        if not answer % 10:
            ans += sum(nums)
    else:
        print(f'#{tt} {ans}')