from collections import deque
def solution(cache, cities):
    if not cache:
        return 5 * len(cities)
    queue = deque()
    answer = 0
    for city in cities:
        city = city.upper()
        if len(queue)< cache:
            if city in queue:
                answer += 1
                queue.remove(city)
                queue.append(city)
                continue
            queue.append(city)
            answer += 5
            continue
        else:
            if city in queue:
                answer += 1
                queue.remove(city)
                queue.append(city)
            else:
                queue.popleft()
                queue.append(city)
                answer += 5
    return answer