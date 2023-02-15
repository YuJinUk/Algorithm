def solution(n, stations, w):
    result = 0
    if stations[0]-w-1>0:
        if not (stations[0]-w-1)%(2*w+1):
            result += (stations[0]-w-1)//(2*w+1)
        elif (stations[0]-w-1)%(2*w+1):
            result += (stations[0]-w-1)//(2*w+1) +1
    for i in range(len(stations)-1):
        start = stations[i]+w
        end = stations[i+1]-w
        if start >= end:
            continue
        elif not (end-start-1)%(2*w+1):
            result += (end-start-1)//(2*w+1)
        elif (end-start-1)%(2*w+1):
            result += (end-start-1)//(2*w+1) +1
    if n-stations[-1]-w > 0:
        if not (n-stations[-1]-w) % (2*w+1):
            result += (n-stations[-1]-w)//(2*w+1)
        elif (n-stations[-1]-w) % (2*w+1):
            result += (n-stations[-1]-w)//(2*w+1) +1
    return result