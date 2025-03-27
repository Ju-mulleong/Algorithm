import sys
sys.stdin = open('input.txt', 'r')

'''
완전탐색으로 한다면, 최단거리니까 BFS 사용
'''


def bfs(start_i, start_j):
    # q 만들기
    q = [start_i, start_j]

    # 가중치 합계 기록할 visited 만들기
    visited = [[0]*N for _ in range(N)]
    visited[start_i][start_j] = arr[start_i][start_j]

    while q:
        # deQueue
        cur_i, cur_j = q.pop()

        # 델타 적용(우, 하)
        di = [0, 1]
        dj = [1, 0]

        for d in range(2):
            ni = cur_i + di[d]
            nj = cur_j + dj[d]

            # 정상인덱스일 때만 실행
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue

            if





    pass

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    bfs(0, 0)