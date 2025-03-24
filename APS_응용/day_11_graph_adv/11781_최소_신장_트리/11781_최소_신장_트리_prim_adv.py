import sys
sys.stdin = open('input.txt', 'r')
import heapq

'''
MST를 최적화된 prim을 써서 만들기
최적화된 prim 
    기존 prim은 단순히 visited와 pq를 사용해서
    최소 가중치인 간선을 선택하고, 표시하고 반복
    최적화된 prim은 여기에 최소가중치를 기록할 lst를 만든다.
    weight_lst는 enQueue할 노드를 거르는 역할을 한다.
    처음에 inf로 초기화하고, weight_lst에 저장된 값보다 적은 가중치일때만 enQueue하고, weight_lst도 업데이트한다.
    
'''


def prim_adv(start_node):
    # pq 생성
    pq = [(0, start_node)]

    # visited 생성
    visited = [0] * (1 + V)

    # 방문한 노드의 최소 가중치 기록할 가중치 리스트 생성
    weight_lst = [float('inf')]*(1+V)
    # print(weight_lst)
    weight_lst[start_node] = 0
    cnt = 0     # MST에 포함된 정점 수
    sum_v = 0

    while pq and cnt < V+1:
        # heappop
        # heappop으로 최소인 가중치 기준 가장 작은 것부터 뽑는다
        cur_weight, cur_node = heapq.heappop(pq)

        # 이미 방문한 경우
        if visited[cur_node]:
            continue

        # visited 처리
        visited[cur_node] = 1
        # sum_v 처리
        sum_v += cur_weight
        # MST에 포함된 정점 개수 증가
        cnt += 1

        for next_info in adj_lst[cur_node]:
            next_weight = next_info[0]
            next_node = next_info[1]

            # 인접노드지만, 이미 방문했다면 continue
            if visited[next_node]:
                continue

            # weight_lst에 기록된 기존 가중치와 비교
            # 더 작을때만 enQueue 하도록
            if next_weight >= weight_lst[next_node]:
                continue

            # weight_lst 처리
            weight_lst[next_node] = next_weight

            # enQueue
            heapq.heappush(pq, (next_weight, next_node))

    return sum_v


T = int(input())

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    # V+1는 노드의 개수(V는 노드의 마지막 번호, 0번부터 존재한다.), E는 간선의 개수

    adj_lst = [[] for _ in range(1+V)]
    # 인접리스트 만들기
    for i in range(E):
        n1, n2, weight = map(int, input().split())
        adj_lst[n1].append((weight, n2))
        adj_lst[n2].append((weight, n1))    # 무방향 리스트다.

    # print(adj_lst)

    # prim_adv
    ans = prim_adv(0)

    print(f'#{test_case} {ans}')