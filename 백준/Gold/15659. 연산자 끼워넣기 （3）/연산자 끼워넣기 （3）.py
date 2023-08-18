import sys
input = sys.stdin.readline

def f(x, y):
    new = []
    for i, j in zip(x, y):
        new.append(str(i))
        new.append(j)
    new.append(str(x[-1]))
    return new

n = input().rstrip()
n = int(n)
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
cnt = [plus, minus, multi, div]
plus = ['+' for _ in range(plus)]
minus = ['-' for _ in range(minus)]
multi = ['*' for _ in range(multi)]
div = ['//' for _ in range(div)]
check = plus + minus + multi + div
minn, maxx = 1e9, (-1)*1e9
def al(result, idx):
    global minn, maxx, n
    if idx == n:
        minn = min(minn, eval(result))
        maxx = max(maxx, eval(result))
        return
    for i in range(4):
        if not cnt[i]:
            continue
        if i == 0:
            m = result + '+'
            cnt[i] -= 1
        elif i == 1:
            m = result + '-'
            cnt[i] -= 1
        elif i == 2:
            m = result + '*'
            cnt[i] -= 1
        else:
            m = result + '//'
            cnt[i] -= 1
        m += str(nums[idx])
        al(m, idx+1)
        cnt[i] += 1
        
al(str(nums[0]), 1)
print(maxx)
print(minn)