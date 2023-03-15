from sys import stdin
n = int(stdin.readline())
dot = [list(map(int,stdin.readline().split())) for i in range(n)]
dot.sort()
def euclidean(d1, d2):
    return (d1[0] - d2[0])**2 + (d1[1] - d2[1])**2

def m(start,end):
    if end == start + 1:
        return euclidean(dot[start],dot[end])
    elif end == start:
        return float('inf')
    mid = (start + end)//2
    min_e = min(m(start, mid), m(mid+1,end))

    poss = []
    for i in range(start, end+1):
        if (dot[mid][0] - dot[i][0])**2 < min_e:
            poss.append(dot[i])
    
    poss.sort(key=lambda x: x[1])
    for i in range(len(poss)-1):
        for j in range(i+1,len(poss)):
            if (poss[i][1] - poss[j][1])**2 < min_e:
                distance = euclidean(poss[i], poss[j])
                min_e = min_e if min_e < distance else distance
            else:
                break
    return min_e
print(m(0, n-1))
# if not n%2:
    # print(m(0,n-1))
# else:
    # check = m(0, n-2)
    # l = euclidean(dot[n-2], dot[n-1])
    # if check > l:
        # print(l)
    # else:
        # print(check)