from collections import deque
def solution(people, limit):
    
    people = deque(sorted(people))
    
    light = 0
    heavy = len(people) - 1
    result = 0
    
    while len(people) >= 1:
        if len(people) == 1:
            return result + 1
        if people[light] + people[heavy] <= limit:
            result += 1
            people.pop()
            people.popleft()
            heavy -= 1
        else :
            result += 1
            people.pop()
        heavy -= 1
    return result