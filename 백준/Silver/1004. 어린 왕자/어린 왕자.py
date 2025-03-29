import sys

input = sys.stdin.readline

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
    result = 0
    for _ in range(N):
        cx, cy, cr = map(int, input().split())
        start_result, end_result = calculate_distance(start_x, start_y, cx, cy, cr), calculate_distance(end_x, end_y, cx, cy, cr)
        if start_result == end_result:
            continue
        result += 1
    
    answer.append(result)

for ans in answer:
    print(ans)