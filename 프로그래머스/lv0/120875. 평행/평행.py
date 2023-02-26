def solution(dot):
    combi = [(0,1),(0,2),(0,3)]
    combi_2 = [(2,3),(1,3),(1,2)]
    result = set()
    for i, j in zip(combi,combi_2):
        if (dot[i[0]][0]-dot[i[1]][0])/(dot[i[0]][1]-dot[i[1]][1]) == (dot[j[0]][0]-dot[j[1]][0])/(dot[j[0]][1]-dot[j[1]][1]):
            return 1
    else: return 0