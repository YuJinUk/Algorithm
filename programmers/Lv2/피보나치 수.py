def solution(n):
    fib = [0,1]
    for i in range(n-1):
        fib.append(fib[i+1] + fib[i])
    return fib[n]%1234567