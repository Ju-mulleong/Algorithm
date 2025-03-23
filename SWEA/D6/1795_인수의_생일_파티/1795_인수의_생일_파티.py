import sys
sys.stdin = open('input.txt', 'r')
import heapq

'''
x번 집으로 최단시간으로 오고 갈때(단방향), 가장 오래걸리는 집의 이동시간 구하기
다익스트라 2번쓰기
처음엔 현재 노드에서 X번, 두 번째는 X번에서 현재 노드
해서 더하기
    더한 값들 최댓값 비교해서 업데이트
'''


def dijkstra(start_node, end_node):
    # pq 만들기
    pq = [(0, start_node)]

    # 누적가중치 리스트 초기화
    weight_lst = [float('inf') for _ in range(N+1)]
    weight_lst[start_node] = 0        # 시작노드 누적가중치는 0

    while pq:
        # heappop
        cur_weight, cur_node = heapq.heappop(pq)
        # print(cur_weight, cur_node)

        # 종료조건
        if cur_node == end_node:
            return cur_weight

        # 가지치기
        # 이미 그 노드에 더 짧은 거리로 도착했다면, continue
        # 우선순위큐는 누적가중치가 작은것부터 pop하기에 남는 찌꺼기 느낌인듯
        if weight_lst[cur_node] < cur_weight:
            continue

        # 현재 노드에 인접한 노드들 heappush
        for next_info in adj_lst[cur_node]:
            next_weight = next_info[0]
            next_node = next_info[1]

            # 다음 노드로 가기 위한 누적 거리
            new_weight = cur_weight + next_weight

            # 새로운 가중치가 목표노드의 누적가중치보다 더 크거나 같으면 continue
            # print(next_node)
            if weight_lst[next_node] <= new_weight:
                continue

            # 가중치 적용
            weight_lst[next_node] = new_weight
            # heappush
            heapq.heappush(pq, (new_weight, next_node))


T = int(input())

for test_case in range(1, 1+T):
    N, M, X = map(int, input().split())
    # N은 노드의 개수, M은 간선의 개수, X는 반드시 들러야할 노드번호

    # 인접리스트 만들기
    # 출발노드번호인 인덱스에 (가중치, 도착노드)순서대로 저장하기
    adj_lst = [[] for _ in range(N+1)]   # 더미인덱스 0 포함

    for _ in range(M):
        start, end, weight = map(int, input().split())
        adj_lst[start].append((weight, end))

    # print(adj_lst)
    max_v = 0
    for i in range(1, N+1):
        if i == X:
            continue
        temp_v = dijkstra(i, X) + dijkstra(X, i)
        # 최댓값 업데이트 시도
        max_v = max(max_v, temp_v)

    # 출력
    print(f'#{test_case} {max_v}')




