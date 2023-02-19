def solution(skill, tr):
    
    cnt = 0
    
    while len(tr):
        
        skill_tree = tr.pop()

        skill_list = [i for i in skill_tree if i in skill]

        if len(skill_list) == 0:
            cnt += 1
            continue

        new_skill = ''.join(skill_list)

        if new_skill in skill and new_skill[0] == skill[0]:
            cnt += 1
    
    return cnt