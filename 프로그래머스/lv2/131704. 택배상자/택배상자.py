from collections import deque
def solution(order):
    order = deque(order)
    subblet = deque()
    truck = 0

    for box in range(1, len(order) +1):
        if order[0] != box:
            subblet.append(box)
            continue
        order.popleft()
        truck += 1  # order에 맞는 box일 경우 트럭으로
        while len(subblet) != 0 and len(order) > 0:
            if order[0] == subblet[-1]:
                subblet.pop()
                truck += 1
                order.popleft()
            else:
                break
    return truck