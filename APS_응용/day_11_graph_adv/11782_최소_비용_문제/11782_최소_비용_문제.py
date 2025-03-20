import sys
sys.stdin = open('input.txt', 'r')
import heapq


'''
다익스트라
항상 (0, 0) 에서 (N-1, N-1)로 이동.
일단 만들어보자
'''


def dijkstra(start_i, start_j):
    # 최소 거리 저장할 dist_lst 초기화
    dist_lst = [[1e18]*N for _ in range(N)]
    dist_lst[start_i][start_j] = 0

    # 우선순위 큐 pq 생성
    pq = [(start_i, start_j)]

    while pq:
        # deQueue
        now_i, now_j = heapq.heappop(pq)

        # 현재 좌표에서 인접한 좌표 구하기
        # 상하좌우 다써야됨. 돌아가는게 더 연료 적게 들수도 있다.
        di = [0, -1, 0, 1]
        dj = [1, 0, -1, 0]

        for d in range(4):
            ni = now_i + di[d]
            nj = now_j + dj[d]

            # 정상인덱스일때만 통과
            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue

            # 가중치 구하기
            # 기본으로 이동할 때 1 + 목표좌표가 현재좌표보다 높으면, 그만큼 가중치 더해야한다.
            add_cost = 0
            if arr[ni][nj] > arr[now_i][now_j]:
                add_cost = arr[ni][nj] - arr[now_i][now_j]

            next_cost = 1 + add_cost

            # dist_lst의 가중치와 비교, next_cost가 더 작을 경우에만 최솟값 업데이트
            if next_cost + dist_lst[now_i][now_j] < dist_lst[ni][nj]:
                dist_lst[ni][nj] = next_cost + dist_lst[now_i][now_j]

                # enQueue
                heapq.heappush(pq, (ni, nj))

    return dist_lst


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N 크기의 맵

    arr = [list(map(int, input().split())) for _ in range(N)]

    dist_lst = dijkstra(0, 0)

    print(f'#{test_case} {dist_lst[N-1][N-1]}')