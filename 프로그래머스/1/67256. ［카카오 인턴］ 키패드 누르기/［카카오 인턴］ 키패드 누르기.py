def solution(numbers, hand):
    dic, dist, answer = {}, {}, ""
    left, mid, right = [1, 4, 7], [2, 5, 8, 0], [3, 6, 9]
    for i in left:
        dic[i] = "L"
    for i in right:
        dic[i] = "R"
    for i in range(1, 10):
        if i % 3 == 1:
            dist[i] = ((i-1)//3, 0)
        elif i % 3 == 2:
            dist[i] = ((i-1)//3, 1)
        else:
            dist[i] = ((i-1)//3, 2)
    dist[0] = (3, 1)
    dist['*'] = (3, 0)
    dist['#'] = (3, 2)
    
    left_start, right_start = '*', '#'
    
    for target in numbers:
        if target in dic:
            answer += dic[target]
            if dic[target] == 'L':
                left_start = target
            else:
                right_start = target
        else:
            xl, yl = dist[left_start]
            xr, yr = dist[right_start]
            xt, yt = dist[target]
            check_l = abs(xl - xt) + abs(yl - yt)
            check_r = abs(xr - xt) + abs(yr - yt)
            if check_l < check_r:
                answer += "L"
                left_start = target
            elif check_l > check_r:
                answer += "R"
                right_start = target
            else:
                if hand == "right":
                    answer += "R"
                    right_start = target
                else:
                    answer += "L"
                    left_start = target
    return answer