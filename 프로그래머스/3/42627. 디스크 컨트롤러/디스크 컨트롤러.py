from collections import deque
import heapq
def solution(jobs):
    jobs_len = len(jobs)
    heapq.heapify(jobs)
    result = deque()
    result.append(heapq.heappop(jobs))
    end = result[-1][0] + result[-1][-1]
    answer = result[-1][-1]
    while jobs:
        possible = []
        while jobs:
            if jobs[0][0] <= end:
                p = heapq.heappop(jobs)
                heapq.heappush(possible, (p[1],p[0],p[1]))
            else:
                break
        if possible:
            finish = heapq.heappop(possible)
            result.append([finish[1], finish[2]])
            for i in possible:
                heapq.heappush(jobs, [i[1],i[2]])
            answer += finish[2]-finish[1]+end
            end += result[-1][-1]
        else:
            result.append(heapq.heappop(jobs))
            end = result[-1][0] + result[-1][1]
            answer += result[-1][-1]

    return answer//jobs_len