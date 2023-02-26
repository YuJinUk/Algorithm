def solution(num, total):
    return list(range(total//num-(num-1)//2, total//num+(num-1)//2+1)) if num % 2 else list(range(total//num - num//2+1, total//num + num//2+1))