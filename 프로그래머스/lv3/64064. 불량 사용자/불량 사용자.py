from collections import Counter
def solution(user_id, banned_id):
    rm_star = dict() # *가 아닌 index를 찾아서 user_id와 비교하기 위한 dictionary 생성
    for ban_id in banned_id:
        b = []
        for i in range(len(ban_id)):
            if ban_id[i] != '*':
                b.append(i)
        rm_star[ban_id] = b
        
    a = Counter(banned_id) # id가 각각 몇개인지 count > 뽑을 개수를 찾기 위함
    
    new = [] # *가 아닌 곳이 같으면 대입, Counter을 통해 banned_id에 맞는 리스트를 각각 생성함
    for i, j in zip(a.keys(), a.values()):
        cnt =0
        aa = []
        idx = rm_star[i]
        for user in user_id:
            if len(user) == len(i):
                for ids in idx:
                    if user[ids] != i[ids]:
                        break
                else:
                    cnt += 1
                    aa.append(user)
        for _ in range(j): # 같은 banned_id의 경우 Counter의 value만큼 대입해줘야 조합가능
            new.append(aa)

    visited = dict() 
    for i in user_id: # 모든 user_id를 key값으로 두고 각 value를 False값으로 지정하여 백트래킹 준비
        visited.setdefault(i, False)
    result = []
    def backtrack(row): # 백트래킹
        ans = 0
        if row == len(banned_id):
            z = []
            for k, v in visited.items():
                if v:
                    z.append(k)
            result.append(z)
            return 1
        for i in range(len(new[row])):
            if visited[new[row][i]] == False:
                visited[new[row][i]] = True
                ans += backtrack(row+1)
                visited[new[row][i]] = False
        return ans
    backtrack(0)
    # result에 순서만 다르고 중복인 리스트가 포함되어 있기 때문에 이를 제거해줘야함.
    # 따라서 result에서 list를 하나씩 꺼내어 item으로 받고
    # item을 set으로 형변환하여 자동으로 sort되게한 후 tuple로 변환하고 list에 담으면 set으로 다시 변환할 수 있음
    # 마지막 set을 통해 중복을 제거해주고 다시 list로 반환하면 중복이 제거됨
    result = list(set([tuple(set(item)) for item in result]))
    return len(result)