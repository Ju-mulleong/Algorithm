import sys
sys.stdin = open('input.txt', 'r')
import heapq

'''
간선의 개수가 100,0000으로 많은것같으니까 
prim 알고리즘 사용
    현재 노드에서 다음 노드로 갈 가중치가 최소인 노드들만 골라서 간다.
    "방문"은 "heappop"때 하는 것
'''


def prim(start_node):
    # visited 생성
    visited = [0]*(1+V)

    # 우선순위 큐 pq 만들기
    pq = [(0, start_node)]

    sum_v = 0
    while pq:
        # deQueue
        cur_weight, cur_node = heapq.heappop(pq)

        # 이미 방문한 노드라면, continue
        if visited[cur_node]:
            continue

        visited[cur_node] = 1
        sum_v += cur_weight

        for next_info in adj_lst[cur_node]:
            next_weight = next_info[0]
            next_node = next_info[1]

            # 인접노드지만 이미 방문했다면 continue
            if visited[next_node]:
                continue

            heapq.heappush(pq, (next_weight, next_node))

    return sum_v


T = int(input())

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    # V는 마지막 노드 번호, E는 간선의 개수
    # 0번노드가 실재하므로, V+1이 노드의 개수이다.

    # 인접리스트 생성
    adj_lst = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_lst[s].append((w, e))   # 가중치, 도착좌표 순서대로 저장
        adj_lst[e].append((w, s))   # 무방향 리스트다.

    # print(adj_lst)

    ans = prim(0)

    print(f'#{test_case} {ans}')
