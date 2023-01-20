# 모르는 개념

- [heapq]([heapq --- 힙 큐 알고리즘 &#8212; 파이썬 설명서 주석판](https://python.flowdas.com/library/heapq.html)

[heapq 정렬 구조]

<img title="" src="file:///C:/Users/wlsdn/OneDrive/바탕 화면/ssafy/algorithm/programmers/Lv2/heap 구조.png" alt="heap 구조.png" width="681">

```python
# 손으로 직접 그려가며 정렬 해봤음
>>> def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# tuple형태로 heap에 insert하면 index == 0인 것을 기준으로 sort되어 정렬된다.
>>> h = [] 
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')
```
