import sys
import heapq

sys.stdin = open("graph.txt", "r")

# Prim 에서 최적화를 추가한 버전
# - 이 버전의 코드가 되어야 간선의 수가 많을 때 유리하다!!!


def prim(start_node):
    pq = [(0, start_node)]  # (비용, 노드)
    key = [float('inf')] * V  # 최소 비용 저장 배열
    MST = [False] * V  # 방문 여부
    min_weight = 0  # 최소 비용 저장

    key[start_node] = 0
    count = 0  # MST에 포함된 정점 개수

    while pq and count < V:
        weight, node = heapq.heappop(pq)

        if MST[node]:  # 이미 방문한 노드는 무시
            continue

        MST[node] = True  # 방문 처리
        min_weight += weight  # 최소 비용 누적
        count += 1  # MST 포함 정점 증가

        for next_node in range(V):
            cost = graph[node][next_node]
            
            # 갈 수 없는 경우 or 이미 방문한 경우 pass
            if cost == 0 or MST[next_node]:
                continue

            # ✅ 기존 key[next_node]보다 작은 값만 업데이트!
            if cost < key[next_node]:
                key[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    return min_weight

# 입력 처리
V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]  # 인접 행렬

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

result = prim(0)  # 출발 정점을 바꾸어도 동일하다.
print(f'최소 비용 = {result}')
