import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
words = []
word_len = 0
dic = {}
for _ in range(N):
    word = input().rstrip()
    check_l = len(word)
    if word not in dic:
        dic[word] = 1
    else:
        continue
    heapq.heappush(words, (check_l, word))
    if check_l > word_len:
        word_len = check_l
result = []
check_len, check_word = heapq.heappop(words)
result.append(check_word)
while words:
    ln, word = heapq.heappop(words)
    if check_len == ln:
        result.append(word)
    elif check_len < ln:
        result.sort()
        for i in result:
            print(i)
        result = [word]
        check_len = ln
for i in result:
    print(i)