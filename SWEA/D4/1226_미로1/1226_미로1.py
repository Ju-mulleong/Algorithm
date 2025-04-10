import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = 10


'''

'''


def bfs():
    # 델타 적용위한 설정
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # 시작점 인덱스 넣은 hq 만들기
    dq = deque([(1, 1)])

    # visited
    visited = [[0]*16 for _ in range(16)]
    visited[1][1] = 1

    while dq:
        # dequeue
        cur_idx = dq.popleft()
        # print(cur_idx)
        cur_i, cur_j = cur_idx

        # 델타로 갈 수 있는지 판단
        # 벽으로 막혀있으니까 비정상인덱스 될 일은 없다.
        for d in range(4):
            ni = cur_i + di[d]
            nj = cur_j + dj[d]
            # print(ni, nj)
            if arr[ni][nj] == 1:
                continue

            # 도착점이라면, return 1
            elif arr[ni][nj] == 3:
                return 1

            # 그 외 갈수 있는 곳이고, 방문하지 않았다면 enQueue
            else:
                if visited[ni][nj]:
                    continue
                dq.append((ni, nj))
                visited[ni][nj] = 1

    # 도착점으로 못빠져나갔으면, return 0
    return 0


for test_case in range(1, 1+T):

    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    # arr은 16*16 미로

    # 출발점, 도착점 = (1, 1), (13, 13)

    # bfs 도착할 수 있는지만 판단하면 되니까
    print(f'#{test_case} {bfs()}')