n, k = map(int, input().split())
prime_num = int(1e9 + 7)
if n == k or not k:
    print(1)
    exit()
elif k == 1:
    print(n)
    exit()
fac_n, fac_k, fac_nk = 1, 1, 1
for i in range(2, n+1):
    fac_n = (fac_n * i) % prime_num
for i in range(2, k+1):
    fac_k = (fac_k * i) % prime_num
for i in range(2, n-k+1):
    fac_nk = (fac_nk * i) % prime_num
fac = fac_nk * fac_k % prime_num

def bi(n, c):
    if c == 0:
        return 1
    elif c == 1:
        return n
    
    tmp = bi(n, c//2)
    if c % 2:
        return tmp * tmp * n % prime_num
    else:
        return tmp * tmp % prime_num

print((fac_n % prime_num) * bi(fac, prime_num-2) % prime_num)