import sys
sys.stdin = open('input.txt', 'r')


def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


# 인접행렬 안쓰고 그냥 델타로?

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())    # 미로의 크기 N
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    # 출발지점 찾기
    i, j = find_start(arr)
    # print(si, sj)

    # visited 만들기
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1   # 시작점에 가중치 1 더하기
    # print(visited)

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    q = [(i, j)]    # 시작점 append하고 시작
    ans = 0

    while q:    # q를 다 비울때까지 실행

        # 만약 deQueue한 값과 인접하고 통로이거나 목적지라면, visited에 가중치 더하기
        # deQueue 실행
        (i, j) = q.pop(0)

        if arr[i][j] == 3:  # 도착하면 탈출
            ans = visited[i][j] - 2
            break

        for d in range(4):      # 4방향 델타
            ni = i + di[d]
            nj = j + dj[d]
            # print(ni, nj)

            # 정상인덱스이고, 통로이거나 목적지이고, 방문 안했으면
            if 0 <= ni <= N-1 and 0 <= nj <= N-1 and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                # print(visited)

    print(f'#{test_case} {ans}')

