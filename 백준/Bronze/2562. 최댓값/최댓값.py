answer = [0,0]
for idx in range(1,10):
    num = int(input())
    if answer[0] < num: answer[0] = num; answer[1] = idx
print(answer[0])
print(answer[1])