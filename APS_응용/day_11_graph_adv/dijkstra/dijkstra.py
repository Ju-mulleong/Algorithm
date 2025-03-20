import sys
sys.stdin = open('graph2.txt', 'r')


def dijkstra(start_node):
    pq = [(0, start_node)]      # 누적거리, 노드번호
    dists = [INF] * V           # 각 정점까지의 최단 거리를 저장할 리스트
    dists[start_node] = 0      # 시작노드 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        # 예제 그림: c로 가는 경로가 3 or 4
        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]  # 다음 노드로 가기위한 가중치
            next_node = next_info[1]    # 다음 노드 번호

            # 다음 노드로 가기위한 누적 거리
            new_dist = dist + next_dist

            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면 continue
            if dists[next_node] <= new_dist:
                continue

            # next_node까지 도착하는데 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists


import heapq
INF = int(21e8)     # 21억 (무한대를 의미한다고 가정)

V, E = map(int, input().split())    # 노드 수, 간선 수
start_node = 0      # 문제에 따라 다름
graph = [[] for _ in range(V)]      # 인접 리스트로 구현

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))     # 가중치(거리), 도착노드 순서, # 단방향 그래프 !!!!!!!

# result_dists: 0에서 출발해서, 다른 노드들까지의 최단거리를 모두 구한다.
result_dists = dijkstra(0)
print(result_dists)

# 그럼 음수 + 양수는 왜 안될까?
# 그리디로 접근할 수 없다. 현재에서
# 최단을 뽑았는데, 만약 현재에서 최단이 아닌 다른노드가 음수로 이어진다면,
# 음수노드와 합쳐져서 현재 선택한 최단을 넘을 수 있기 때문
# 그래서 벨만써야함



