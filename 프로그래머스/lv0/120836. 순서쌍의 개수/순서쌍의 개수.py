def solution(n):
    answer = sum([2 for i in range(1, int(n**0.5)+1) if not n%i])
    return answer-1 if int(n**0.5)**2 == n else answer 