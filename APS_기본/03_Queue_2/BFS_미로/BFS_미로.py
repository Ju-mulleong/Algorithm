import sys
sys.stdin = open('input.txt', 'r')


def bfs(i, j, N):       # 시작위치 i, j, 크기 N
    visited = [[0]*N for _ in range(N)]     # visited 생성
    q = []                                  # 큐 생성
    q.append([i, j])                        # 시작점 인큐
    visited[i][j] = 1                       # 시작점 인큐 표시
    while q:                                # 큐에 남은 칸이 없을 때 까지..큐가 비워질 때 까지
        ti, tj = q.pop(0)                   # t <- deQueue
        if maze[ti][tj] == '3':                 # t에서 할 일...
            # return 1                          # 출구(3)에 도착하면 1, 아니면 0 return한다고 가정
            return visited[ti][tj] - 2          # 입구에서 출구 사이의 빈 칸 수(출발점, 도착점 2 뺀다.)
        # t에 인접 w중, enQueue되지 않은 곳이면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 늘 먹던 델타
            wi, wj = ti + di, tj + dj
            # 미로를 벗어나지 않고, 벽이 아니고,
            if 0 <= wi <= N-1 and 0 <= wj <= N-1 and maze[wi][wj]!= '1' and visited[wi][wj] == 0:
                # enQueue, 표시
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    return 0


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


T = int(input())
for test_case in range(1, 1+T):
    N = int(input())    # 미로의 크기
    maze = [input() for _ in range(N)]

    sti, stj = find_start(N)

    ans = bfs(sti, stj, N)
    print(f'#{test_case} {ans}')
