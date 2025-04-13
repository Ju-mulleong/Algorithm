import sys
sys.stdin = open('input.txt', 'r')
import heapq


'''
BFS로 해보기
- 다익스트라?
'''


def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':

                return i, j


def dijkstra():
    # pq 설정
    pq = [(0, s_i, s_j, K, 1)]

    # 각 좌표까지의 최단 커맨드 저장할 리스트
    # 4차원[i][j][tree][d]
    weights = [[[[float('inf')]*4 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
    weights[s_i][s_j][K][1] = 0
    min_v = float('inf')

    while pq:
        # deQueue
        cur_cnt, cur_i, cur_j, cur_k, cur_d = heapq.heappop(pq)

        # # 이미 더 작은 경로로 온 적 있다면, pass
        if weights[cur_i][cur_j][cur_k][cur_d] < cur_cnt:
            continue

        # 이미 도착지까지의 커맨드수보다 현재 커맨드가 더 크거나 같으면, continue
        if min_v <= cur_cnt:
            continue

        # 도착지라면, 최솟값 비교
        if arr[cur_i][cur_j] == 'Y':
            min_v = min(min_v, cur_cnt)


        # 델타 방향 확인
        for d in range(4):
            ni = cur_i + di[d]
            nj = cur_j + dj[d]

            # 맵 벗어나면 pass
            if 0 > ni or ni >= N or 0 > nj or nj >= N:
                continue

            # 나무라면, 베기 / 더이상 벨 수 있는 횟수가 남아있지 않으면, pass
            if arr[ni][nj] == 'T':
                if cur_k == 0:
                    continue
                next_k = cur_k - 1

            # 아니라면, 그대로
            else:
                next_k = cur_k

            # 방향 전환 명령 수 계산

            # 처음 방향과 같은 방향이라면
            # 방향돌리는데 커맨드 사용하지 않음(n = 0)
            if cur_d == d:
                n = 0

            # 처음 방향과 다른 방향이라면
            # 방향 돌리는데 사용한 커맨드(n)
            else:
                # 0 -> 3 or 3 -> 0
                if cur_d in (0, 3) and d in (0, 3):
                    n = 1
                # 그 외는 그냥 방향 인덱스 차이만큼
                else:
                    n = abs(cur_d - d)

            # 이동한 만큼 커맨드 더하기
            next_cnt = cur_cnt + (1+n)

            # 이미 이동 예정 좌표에 더 적거나 같은 커맨드(cnt)로 온 적 있다면
            if weights[ni][nj][next_k][d] <= next_cnt:
                continue

            # weights 갱신
            weights[ni][nj][next_k][d] = next_cnt

            # enQueue
            heapq.heappush(pq, (next_cnt, ni, nj, next_k, d))

    return min_v


T = int(input())

for test_case in range(1, 1+T):
    # 필드의 크기 N, 나무를 벨 수 있는 횟수 K
    N, K = map(int, input().split())

    # N*N크기의 맵
    arr = [list(input()) for _ in range(N)]

    # 출발점, 목적지 찾기
    s_i, s_j = find_start()

    # 델타
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # dijkstra
    ans = dijkstra()

    if ans == float('inf'):
        ans = -1

    print(f'#{test_case} {ans}')

'''
# 목적지에 이미 도착했다면, 더 이동할 필요없으므로 pq에서 지우기
        # 할 필요없다. 모든 경우에 if 검사해서 늘어나는 시간이 있어서 별 차이 없음
        # if arr[cur_i][cur_j] == 'Y':
        #     continue
'''