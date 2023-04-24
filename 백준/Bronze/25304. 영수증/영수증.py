cost, n, answer = int(input()), int(input()), 0
for _ in range(n):
    x, y = map(int, input().split())
    answer += x * y
print('Yes') if answer == cost else print('No')