n = int(input())
if n == 1:
    print(1)
    exit()
elif n == 2:
    print(3)
    exit()
a, b = 1, 3
for i in range(3, n+1):
    a, b = b, a*2 + b
print(b % (int(1e4)+7))