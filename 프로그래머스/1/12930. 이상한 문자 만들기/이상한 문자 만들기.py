def solution(s):
    s_list = s.split(' ')
    ans = []
    for i in s_list:
        isy = ''
        for j in range(len(i)):
            if j % 2 == 0 or j == 0: 
                isy += i[j].upper()
            else: 
                isy += i[j].lower()
        ans.append(isy)
    return ' '.join(ans)