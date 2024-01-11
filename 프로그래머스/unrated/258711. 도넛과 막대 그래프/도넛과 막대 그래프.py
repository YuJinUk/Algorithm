from collections import deque, defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    
    '''
    edges = [a, b] : a 번 정점에서 b번 정점으로 향하는 선
    '''
    
    '''
    answer = [정점, 도넛, 막대, 8자]
    '''
    
    '''
    생성된 정점 : 2개 이상의 나가는 것만 있고 들어오는 것은 없어야함.
    막대 : 출발노드한테 돌아오지 않음.
    도넛 : 출발노드한테 돌아오며 순환하는 노드들이 나가는것 1개 들어오는것 1개
    8자 : 출발노드한테 돌아오며 나가는 것이 *(2개 이상)인 노드가 있음 *중요
    '''
    
    input_nodes, output_nodes = defaultdict(list), defaultdict(list)
    for edge in edges:
        inp, outp = edge
        input_nodes[inp].append(outp)
        if outp not in input_nodes: input_nodes[outp] = []
        output_nodes[outp].append(inp)
        if inp not in output_nodes: output_nodes[inp] = []
    
    for node in input_nodes:
        l = len(input_nodes[node])
        if l > 1 and not output_nodes[node]:
            new_node = node
            break
    answer[0] = new_node
    
    for nxt_node in input_nodes[new_node]:
        output_nodes[nxt_node].remove(new_node)
        if nxt_node in output_nodes[nxt_node]:
            answer[1] += 1
            continue
        queue = deque()
        queue.append(nxt_node)
        visited = defaultdict(int)
        visited[nxt_node] = 1
        flag = 0
        while queue:
            nxt = queue.pop()
            input_l = len(input_nodes[nxt])
            output_l = len(output_nodes[nxt])
            
            if not input_l or not output_l: # 들어가거나 나가는거 하나라도 없으면 막대 그래프
                answer[2] += 1
                flag = 1
                break
            
            if input_l: # 방출하는 선이 있으면
                if input_l > 1 and output_l > 1: # 2개 이상이면 8자
                    answer[3] += 1
                    flag = 1
                    break
                for n in input_nodes[nxt]:
                    if not visited[n]:
                        queue.append(n)
                        visited[n] = 1
        if not flag:
            answer[1] += 1
    
    return answer