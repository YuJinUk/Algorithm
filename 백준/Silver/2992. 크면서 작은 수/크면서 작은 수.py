from itertools import permutations
n = list(input())
check = int(''.join(n))
ans = set()
for i in permutations(n, len(n)):
    ans.add(int(''.join(i)))
ans = sorted(list(ans))
try:
    print(ans[ans.index(check)+1])
except IndexError:
    print(0)