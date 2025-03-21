import sys, pprint
sys.stdin = open('graph.txt', 'r')

# prim
# - 특정 정점 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 고르자
# --> 그냥 큐가 아닌, 우선순위 큐를 활용하면 좋다.
# deQueue하고, 그 노드와 연결된 모든 노드를 Q에 집어넣고, visited로 빼는 형태기에
# 넣을때 visited = 1하면 안된다!!!
#

def prim(start_node):
    pq = [(0, start_node)]  # 시작점은 가중치가 0이다. 시작노드의 가중치, 시작노드
    MST = [0] * V       # visited와 동일
    min_weight = 0      # 최소 비용 저장

    while pq:
        weight, node = heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue

        MST[node] = 1           # 방문 처리
        min_weight += weight    # 누적합 추가

        for next_node in range(V):
            # 갈 수 없으면 pass
            if graph[node][next_node] == 0:
                continue

            # 이미 방문했으면 pass
            if MST[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))     # 다음노드의 가중치, 다음 노드

    print(MST)
    return min_weight


import heapq

V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]     # 인접 행렬
                                        # [선택과제] 인접 리스트

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight  # 무방향그래프니까 양 쪽 모두에 할당

print(f'graph')
pprint.pprint(graph)
result = prim(0)
print(f'최소 비용 = {result}')

'''
만약 heapq를 안쓴다면
만약 dq에 같은 노드에, 더 적은 가중치로 들어오면 원래 dq에 있던 노드를
더 적은 가중치로 변경시킨다.
'''