from math import comb
a = int(input()) / 100
b = int(input()) / 100
sum_a, sum_b = 0, 0
sosu = [2,3,5,7,11,13,17]
for i in sosu:
    sum_a += a**i * (1 - a)**(18 - i) * comb(18, i)
    sum_b += b**i * (1 - b)**(18 - i) * comb(18, i)
print(1 - (1-sum_a)*(1-sum_b))