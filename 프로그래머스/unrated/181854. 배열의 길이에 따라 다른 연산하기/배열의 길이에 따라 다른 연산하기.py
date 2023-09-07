def solution(arr, n):
    if len(arr) % 2: return [i+n if not idx % 2 else i for idx, i in enumerate(arr)]
    else: return [i+n if idx % 2 else i for idx, i in enumerate(arr)]