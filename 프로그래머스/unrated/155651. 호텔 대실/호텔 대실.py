from collections import defaultdict

def changetime(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute
    
def solution(book_time):
    answer, now, books = 0, 0, defaultdict(int)

    for t in book_time:
        start, end = changetime(t[0]), changetime(t[1])
        books[start] += 1
        books[end + 10] -= 1 # 청소 시간 보정

    books = sorted(list(map(list, books.items())))

    for b in books:
        now += b[1]
        if answer < now:
            answer = now

    return answer