def solution(s):
    answer = 0
    l = len(s)
    if l == 1:
        return 1

    for leng in range(l, 1, -1):
        for j in range(l-leng+1):
            if s[j] == s[j+leng-1]:
                if s[j:j+leng] == s[j:j+leng][::-1]:
                    return leng
    else:
        return 1
# def solution(s):
#     l = len(s)
#     matrix = [[0] * l for _ in range(l)]
#     for i in range(l):
#         matrix[i][i] = 1

#     for leng in range(2, l+1):
#         for i in range(l-leng+1):
#             j = i+leng-1
#             if s[i] == s[j] and leng == 2:
#                 matrix[i][j] = 2
#             elif s[i] == s[j]:
#                 matrix[i][j] = matrix[i+1][j-1]+2
#             else:
#                 matrix[i][j] = max(matrix[i][j-1], matrix[i+1][j])
#     return matrix[0][-1]