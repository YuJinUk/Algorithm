a, b, c = map(int, input().split())
if a == b and b == c: print(10000 + 1000 * a)
elif (a == b and b != c): print(1000 + 100 * a)
elif(b == c and c != a): print(1000 + 100 * b)
elif(c == a and a != b): print(1000 + 100 * c)
elif a != b and b != c and c != a: print(100 * max(a, b, c))