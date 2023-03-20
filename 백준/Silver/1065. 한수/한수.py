n = int(input())
answer = 0
for i in range(1, n+1):
    if not i // 100:
        answer += 1
    else:
        check = str(i)
        if int(check[1]) - int(check[0]) == int(check[2]) - int(check[1]):
            answer += 1
print(answer)