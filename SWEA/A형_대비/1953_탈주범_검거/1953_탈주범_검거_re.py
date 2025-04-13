import sys, pprint
sys.stdin = open('input.txt', 'r')
from collections import deque


'''
숫자로 각 터널 구조물 종류를 구분한다.
현재 터널의 출구방향과 이동할 터널의 입구가 서로 통해야함.
BFS
visited에 이 좌표까지 이동하는데 걸린 시간 기록
'''


def bfs(s_i, s_j):
    dq = deque([(s_i, s_j)])
    visited[s_i][s_j] = 1
    cnt = 1

    while dq:
        # deQueue
        cur_i, cur_j = dq.popleft()

        # 현재 좌표의 visited의 값이 L과 같다면, 최대 소요가능한 시간 사용한 것이므로 pass
        if visited[cur_i][cur_j] == L:
            continue

        cur_t = arr[cur_i][cur_j]

        # 현재 터널에서 갈 수 있는 방향만 탐색
        for d in d_dict[cur_t]:
            ni = cur_i + di[d]
            nj = cur_j + dj[d]

            # 맵 벗어나거나, 이미 방문했다면 pass
            if 0 > ni or ni >= N or 0 > nj or nj >= M or visited[ni][nj]:
                continue

            # 이동 목표 좌표의 터널 확인
            # 그 터널이 현재 터널과 이어져있는지 확인
            # 상-하 / 좌-우
            # 1-3 / 0-2
            if d >= 2:
                dd = d-2
            else:
                dd = d+2

            if dd not in d_dict[arr[ni][nj]]:
                continue

            # 이어져있다면, 이동하고(enQueue), 방문처리, cnt += 1
            dq.append((ni, nj))
            visited[ni][nj] = visited[cur_i][cur_j] + 1
            cnt += 1

    # pprint.pprint(visited)
    return cnt

T = int(input())

for test_case in range(1, 1+T):
    N, M, s_i, s_j, L = map(int, input().split())
    # 맵의 세로크기 N, 가로크기 M, 시작 i, 시작 j, 탈출 후 소요된 시간 L

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    d_dict = {
        1: [0, 1, 2, 3], 2: [1, 3], 3: [0, 2], 4: [0, 1], 5: [0, 3], 6: [2, 3], 7: [1, 2],
        0: []
    }

    visited = [[0]*M for _ in range(N)]
    ans = bfs(s_i, s_j)

    print(f'#{test_case} {ans}')

