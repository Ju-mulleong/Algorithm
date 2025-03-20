import sys
import heapq
sys.stdin = open('input.txt', 'r')


'''
최소거리를 구하므로 다익스트라 써야됨.
'''


def dijkstra(start_node):
    # 모든 노드의 거리 가중치 inf로 초기화
    distance_lst = [1e18] * (1 + N)
    distance_lst[start_node] = 0

    # 우선순위 q 만들기
    pq = [(0, start_node)]

    while pq:
        # deQueue
        dist, node = heapq.heappop(pq)

        # (인접 노드의 가중치+ 현재 target의 가중치, 인접 노드번호) =>enQueue
        for next_info in adj_lst[node]:
            next_dist = next_info[0]    # 다음 노드로 가야하는 거리
            next_node = next_info[1]    # 다음 노드 번호

            # 다음 노드로 가기위한 누적 거리
            new_dist = dist + next_dist

            # 만약 next_node의 가중치가 지금 계산한 가중치보다 작거나 같으면, continue
            if distance_lst[next_node] <= new_dist:
                continue

            # new_dist가 더 작다면, distance_lst에 업데이트
            distance_lst[next_node] = new_dist

            # enQueue
            heapq.heappush(pq, (new_dist, next_node))

    return distance_lst


T = int(input())

for test_case in range(1, 1+T):
    N, E = map(int, input().split())
    # N은 목적지(0번노드 포함이므로, 노드의 개수 -1 = N), E는 간선의 개수

    # 0부터 N까지의 최소거리 구하기.
    adj_lst = [[] for _ in range(1+N)]

    for i in range(E):
        start, end, weight = map(int, input().split())
        # start는 시작 노드, end는 도착 노드, weight는 이 경로의 거리

        # 무방향 그래프
        # 인접리스트에 시작노드 = 인덱스에 (목적지, 거리)로 저장
        adj_lst[start].append((weight, end))

    # print(adj_lst)

    # dijkstra
    distance_lst = dijkstra(0)

    print(f'#{test_case} {distance_lst[-1]}')