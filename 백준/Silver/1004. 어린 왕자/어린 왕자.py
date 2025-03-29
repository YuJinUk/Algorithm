import sys

TC = int(input())

answer = []

def calculate_distance(x, y, a, b, r):
    euclidean_distance = ((x - a)**2 + (y - b)**2)**(0.5)
    if euclidean_distance < r:
        return True
    return False

for _ in range(TC):
    start_x, start_y, end_x, end_y = map(int, input().split())
    
    N = int(input())

    planet = []
    for _ in range(N):
        cx, cy, cr = map(int, input().split())
        planet.append((cx, cy, cr))
    
    start_point_cnt, end_point_cnt = 0, 0
    
    for cx, cy, cr in planet:
        if calculate_distance(start_x, start_y, cx, cy, cr) and not calculate_distance(end_x, end_y, cx, cy, cr):
            start_point_cnt += 1
        elif not calculate_distance(start_x, start_y, cx, cy, cr) and calculate_distance(end_x, end_y, cx, cy, cr):
            end_point_cnt += 1
    
    answer.append(start_point_cnt + end_point_cnt)

for ans in answer:
    print(ans)