n = int(input())
farm_shape = [list(map(int, input().split())) for _ in range(6)]

def find_cut(list_a, list_b): #(나, 이전)
    if list_a[0] == 1 and list_b[0] == 4:
        return True
    elif list_a[0] == 2 and list_b[0] == 3:
        return True
    elif list_a[0] == 3 and list_b[0] == 1:
        return True
    elif list_a[0] == 4 and list_b[0] == 2:
        return True
    else:
        return False    

list_1_2 = []
list_3_4 = []
for i in farm_shape:
    if i[0] == 2 or i[0] == 1 : # 동 or 서로 이동한 것중 가장 큰 수를 찾으면됨
        list_1_2.append(i[1])
    else:
        list_3_4.append(i[1]) # 남 or 북으로 이동한 것 중 가장 큰 수를 찾으면 됨
sum_all = max(list_1_2) * max(list_3_4)

for i in range(len(farm_shape)):
    if find_cut(farm_shape[i], farm_shape[i-1]):
        sum_cut = farm_shape[i-1][1] * farm_shape[i][1] # 잘린 부분
        break
print((sum_all - sum_cut)*n)