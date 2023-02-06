n = int(input()) # 회의 개수
timetable = [list(map(int, input().split())) for _ in range(n)]

timetable.sort(reverse = True)
i = 0
result = 0
while True:
    new = []
    j = i+1
    new.append(timetable[i])

    while j<n:
        if timetable[j][1] <= new[-1][0]:
            new.append(timetable[j])
        j+=1
        
    if result < len(new):
        result = len(new)
    i += 1
    if i<n:
        break

print(result)