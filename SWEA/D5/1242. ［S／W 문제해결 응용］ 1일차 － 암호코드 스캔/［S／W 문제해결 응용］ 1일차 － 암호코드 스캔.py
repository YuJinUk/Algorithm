dict = {'112':0, '122':1, '221':2, '114':3, '231':4, '132':5, '411':6, '213':7, '312':8, '211':9}
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    answer = 0
    code_list = set()
    for r in range(N):
        for c in range(M - 1, -1, -1):
            if code[r][c] != "0":
                code_list.add(code[r][:c + 1])
                break
            continue
    patterns = []
    for code in code_list:
        new_code = ''
        for i in range(len(code)):
            num = format(int(code[i], 16), 'b')
            while len(num) != 4:
                num = '0' + num
            new_code += num
        result = []
        c1 = c2 = c3 = 0
        for i in range(len(new_code)-1, -1, -1):
            if c2 == 0 and c3 == 0 and new_code[i] == '1':
                c1 += 1
            elif c1 > 0 and c3 == 0 and new_code[i] == '0':
                c2 += 1
            elif c1 > 0 and c2 > 0 and new_code[i] == '1':
                c3 += 1
            elif c1 > 0 and c2 > 0 and c3 > 0 and new_code[i] == '0':
                min_cnt = min(c1, c2, c3)
                c1 //= min_cnt
                c2 //= min_cnt
                c3 //= min_cnt
                pattern = dict[str(c1)+str(c2)+str(c3)]
                result.append(pattern)
                c1 = c2 = c3 = 0
                if len(result) == 8:
                    if result not in patterns:
                        patterns.append(result)
                        total = 0
                        for j in range(8):
                            if j % 2:
                                total += result[j] * 3
                            else:
                                total += result[j]
                        if total % 10 == 0:
                            answer += sum(result)
                    result = []
 
    print('#{} {}'.format(tc, answer))