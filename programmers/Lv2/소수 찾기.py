from itertools import permutations
from collections import deque

def sosu(n): # 소수 찾는 함수 소수면 1을 아니면 0을 return
    if n == 0:
        return 0
    elif n == 1:
        return 0
    
    sosu_n = 0
    
    for i in range(1,int(n**0.5 +1)): # n**0.5보다 작은 수만 찾아서 1밖에 없으면 소수 
        if n % i == 0:
            sosu_n += 1
    if sosu_n == 1:
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(numbers)
    dq = deque()
    new_dq = deque()
    for i in range(1,len(numbers)+1): # permutations를 통해 보든 경우의 수를 구함 deque의 경우 list보다 append와 pop이 빠르기 때문에 이용
        dq += deque(map(''.join,deque(permutations(numbers,i))))
    
    # 가장 왼쪽 숫자를 뽑아내고 문자로 permutations을 형성했기에 맨 앞에 0인 수를 제거하기 위해 int(a)로 반환하여 새로운 deque에 없다면 소수인지 확인하여 맨 뒤에 추가
    for i in range(len(dq)): 
        a = dq.popleft()
        if int(a) not in new_dq:
            b = sosu(int(a))
            dq.append(b)
            new_dq.append(int(a))

    return sum(dq) # 소수이면 1을 반환했으므로 sum을 통해 소수의 갯수를 return