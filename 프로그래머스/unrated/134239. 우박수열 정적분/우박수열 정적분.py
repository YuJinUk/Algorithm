dp = []
def dp_list(k):
    global dp
    if k % 2 == 0:
        k = k/2
    else:
        k = k*3 +1
    dp.append(k)
    if k == 1:
        return dp
    else:
        return dp_list(k)

def solution(k, ranges):
    ans = []
    dp = [k] + dp_list(k)
    for range_r in ranges:
        result = 0
        f = range_r[0]
        s = len(dp) + range_r[1]
        if f > s-1:
            ans.append(-1)
        elif f == s-1:
            ans.append(0)
        else:
            for i in range(f, s):
                result += dp[i] * 2
            result -= dp[f]
            result -= dp[s-1]
            ans.append(result/2)
    return ans