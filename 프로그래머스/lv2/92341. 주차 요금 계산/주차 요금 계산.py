import heapq
def f(x):
    h, m = x.split(':')
    return int(h) * 60 + int(m)

def solution(fees, records):
    cars = set()
    dic = {}
    answer = []
    for record in records:
        t, n, s = record.split(' ')
        t = f(t)
        if n not in dic:
            dic[n] = []
        heapq.heappush(dic[n], (t, s))
        cars.add(n)
    cars = sorted(list(cars))
    result = [0 for _ in range(len(cars))]
    for idx, car in enumerate(cars):
        while dic[car]:
            T, S = heapq.heappop(dic[car])
            if S == 'IN':
                check = T
            else:
                result[idx] += T - check
        if S == 'IN':
            result[idx] += 24 * 60 - 1 - T
    for i in result:
        if i <= fees[0]:
            answer.append(fees[1])
            continue
        mok, mod = divmod(i - fees[0], fees[2])
        if mod:
            mok += 1
        answer.append(mok * fees[3] + fees[1])
    return answer
            