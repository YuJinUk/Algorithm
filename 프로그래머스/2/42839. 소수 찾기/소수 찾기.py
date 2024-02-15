from itertools import permutations
from collections import deque
def sosu(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    
    sosu_n = 0
    
    for i in range(1,int(n**0.5 +1)):
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
    for i in range(1,len(numbers)+1):
        dq += deque(map(''.join,deque(permutations(numbers,i))))
    
    for i in range(len(dq)):
        a = dq.popleft()
        if int(a) not in new_dq:
            b = sosu(int(a))
            dq.append(b)
            new_dq.append(int(a))

    return sum(dq)