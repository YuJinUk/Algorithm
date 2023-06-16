import sys
N = sys.stdin.readline().split()
l = len(N[0])
mok = l//10
answer = [N[0][i*10:i*10+10] for i in range(mok+1)]
for x in answer:
    print(x)