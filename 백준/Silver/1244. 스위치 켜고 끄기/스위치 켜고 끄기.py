N = int(input()) # 스위치 개수
state = list(map(int, input().split())) # 입력받은 스위치 상태
nums = int(input()) # 학생수
n = [list(map(int, input().split())) for _ in range(nums)] # len(n) == nums

def switch(x): # 1, 0을 switch해주는 func
    if x == 1: return 0
    else: return 1

for i in n:
    if i[0] == 1: # 남자면
        idx = i[1] -1 # 본인의 index를 찾고
        while True: # N이전의 모든 배수를 찾아 1과 0을 switch
            state[idx] = switch(state[idx])
            if idx + i[1] > N-1:
                break
            idx += i[1]
    else: # 여자면
        idx = i[1] - 1
        state[idx] = switch(state[idx]) # 본인은 무조건 switch
        i = 1
        while True: # 양쪽을 한칸씩 넓혀가면서 만약 0~N을 벗어나지 않고 대칭점이 같으면 switch
            if idx-i >= 0 and idx+i < N and state[idx-i] == state[idx+i]:
                state[idx-i] = switch(state[idx-i])
                state[idx+i] = switch(state[idx+i])
            else:
                break
            i += 1
mok = N//20 # 20줄씩 출력하기 위해 몫을 이용
for i in range(mok+1):
    print(' '.join(map(str,state[i*20 : (i+1)*20])))