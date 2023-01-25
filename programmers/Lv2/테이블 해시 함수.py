def solution(data, col, row_begin, row_end):
    sort_data = sorted(data, key = lambda x : (x[col-1], -x[0]))
    sort_list = []
    for i in range(row_begin, row_end+1):
        summ = 0
        for j in sort_data[i-1]:
            summ += j % (i)
        sort_list.append(summ)
    num = sort_list[0]
    for i in range(1,len(sort_list)):
        num = num ^ sort_list[i]
    return num