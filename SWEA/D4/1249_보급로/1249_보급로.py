import sys
sys.stdin = open('input.txt', 'r')
import heapq


'''
출발지와 도착지간의 최단거리 => 다익스트라
도착지까지의 가중치를 출발점에서부터 계속 더하면서 최소인 경우에만 이동
'''


def dijkstra(start_i, start_j):
    # pq 초기화
    pq = [(0, start_i, start_j)]

    # dist_lst 초기화
    dist_lst = [[1e18]*N for _ in range(N)]
    dist_lst[start_i][start_j] = 0

    while pq:
        # deQueue
        cur_w, cur_i, cur_j = heapq.heappop(pq)

        # 상하좌우 진행중, 정상인덱스일때만 실행
        di = [0, -1, 0, 1]
        dj = [1, 0, -1, 0]

        for d in range(4):
            ni = cur_i + di[d]
            nj = cur_j + dj[d]

            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue

            # 목표인덱스의 가중치와 현재 가중치 더하기
            next_w = cur_w + arr[ni][nj]

            # next_w 가 dist_lst의 가중치보다 크거나 같으면, continue
            if next_w >= dist_lst[ni][nj]:
                continue

            # dist_lst 업데이트, enQueue
            dist_lst[ni][ni] = next_w
            heapq.heappush(pq, (next_w, ni, nj))

    return dist_lst[N-1][N-1]


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N 크기의 지도

    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)

    ans = dijkstra(0, 0)

    print(f'#{test_case} {ans}')
    