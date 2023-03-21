n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for num in A:
    remain = num - b
    answer += 1
    if remain <= 0:
        continue
    if not remain % c:
        answer += remain // c
    else:
        answer += remain // c + 1
    
print(answer)