n = int(input())
m = int(input())
mm = list(str(m))
mm.reverse()
for i in mm:
    print(n * int(i))
print(n*m)