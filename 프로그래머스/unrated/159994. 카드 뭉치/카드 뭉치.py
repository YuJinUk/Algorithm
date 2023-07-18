def solution(cards1, cards2, goal):
    idx1, idx2 = [], []
    for i in cards1:
        if i in goal:
            idx1.append(goal.index(i))
        else:
            idx1.append(len(goal))
    for i in cards2:
        if i in goal:
            idx2.append(goal.index(i))
        else:
            idx2.append(len(goal))
    if idx1 == sorted(idx1) and idx2 == sorted(idx2):
        return "Yes"
    else:
        return "No"
        