def solution(citations):
    answer = 0
    n = len(citations)
    for i in range(n+1):
        count = 0
        for citation in citations:
            if i <= citation:
                count += 1
        if i <= count:
            answer = i
    return answer