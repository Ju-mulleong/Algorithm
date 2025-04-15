import sys, pprint
sys.stdin = open('input2.txt', 'r')
from collections import deque

'''
'S'는 수연이의 위치
    수연이는 1초에 한 칸씩 상하좌우중 한 방향으로 이동 가능
    돌으로는 이동 불가
'D'는 여신의 공간
'X'는 돌의 위치
'*'는 악마의 위치
악마의 손아귀:
    '*'에서 상하좌우로 매 초마다 인접해있는 영역들을 부식시키며 확장되어간다.
    돌은 부식되지 않으며 , 여신의 공간도 마찬가지로 부식되지 않는다.
    악마에서 최초로 상하좌우로 퍼져나가고, 악마의 손아귀자체에서도 상하좌우로 퍼져나간다.

수연이가 여신님께 최소시간으로 이동하면서, '악마의 손아귀'에 닿으면 안된다.
이 최소시간을 구해서 출력, 
만약 수연이가 여신님께 가는 것 자체가 불가능하다면
'GAME OVER' 출력
------------------------------------
최소시간이니까 다익스트라 일단 써보기.
    악마의 손아귀 적용해야되니까 bfs?
단, 매 초마다 악마의 손아귀스킬을 맵에 적용
1초에 1칸 이동하므로, 최소 시간은 최소 거리와 같다.
'''


def find_idx():
    global devil_idx, devil_arr
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'S':
                s_i, s_j = i, j
            elif arr[i][j] == '*':
                devil_idx.append((i, j))
                devil_arr[i][j] = 1
            elif arr[i][j] in ('D', 'X'):
                devil_arr[i][j] = -1

    return s_i, s_j


def devils_hand():
    global devil_idx, devil_arr
    L = len(devil_idx)
    # 악마의 손아귀
    # 처음에 길이구해서 그 만큼만 보도록
    for devil in range(L):
        d_i, d_j = devil_idx[devil]
        # 상하좌우 한칸씩
        for d in range(4):
            ni = d_i + di[d]
            nj = d_j + dj[d]

            # 정상인덱스인지 확인
            if 0 > ni or ni >= N or 0 > nj or nj >= M:
                continue

            # arr[ni][nj]가 빈 땅이거나 수연이 있는 땅이면 확장
            if devil_arr[ni][nj] == 0:
                devil_arr[ni][nj] = 1
                devil_idx.append((ni, nj))


def bfs():
    global min_v
    # dq 생성
    dq = deque([(0, s_i, s_j)])

    # 도달하는데 걸린 최소 시간 저장할 visited
    visited = [[float('inf')]*M for _ in range(N)]
    visited[s_i][s_j] = 0
    pre_d = 0

    while dq:
        # deQueue
        cur_d, cur_i, cur_j = dq.popleft()
        # print(cur_d)

        # 여신님에 닿으면, 최소시간 업데이트 시도하고 q에서 제거
        if arr[cur_i][cur_j] == 'D':
            # print(cur_i, cur_j)
            min_v = min(min_v, cur_d)
            continue

        # 시간초 지나면, 악마의 손아귀 확장
        if cur_d != pre_d:
            pre_d = cur_d
            devils_hand()
        # pprint.pprint(devil_arr)

        # 이동한 위치가 악마의 손아귀에 닿았는지 확인
        if devil_arr[cur_i][cur_j] == 1:
            continue

        # 델타
        for d in range(4):
            ni = cur_i + di[d]
            nj = cur_j + dj[d]
            next_d = cur_d + 1
            # 비정상인덱스 확인
            if 0 > ni or ni >= N or 0 > nj or nj >= M:
                continue

            # 땅이거나 여신님일때만 이동
            if arr[ni][nj] not in ('.', 'D'):
                continue

            # 이미 이 좌표에 더 적거나 같은 시간으로 온 적이 있으면, pass
            if visited[ni][nj] < next_d:
                continue

            # 이동(enQueue)
            visited[ni][nj] = next_d
            dq.append((next_d, ni, nj))


T = int(input())

for test_case in range(1, 1+T):
    # N행 M열의 맵
    N, M = map(int, input().split())

    # 맵
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # 악마의 손아귀 좌표 저장 리스트
    devil_idx = []

    # 악마의 손아귀 표시 할 배열
    devil_arr = [[0]*M for _ in range(N)]

    # 처음 수연이 위치 찾기
    s_i, s_j = find_idx()

    min_v = float('inf')

    # 게임 시작
    bfs()

    if min_v == float('inf'):
        ans = 'GAME OVER'
    else:
        ans = min_v

    print(f'#{test_case} {ans}')