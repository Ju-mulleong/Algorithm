import sys
sys.stdin = open('input.txt', 'r')


'''
N*N보드에 N개의 퀸을 서로 다른 퀸들이 공격하지 못하게 놓는 경우의 수는 몇 가지인가?
DFS?
'''


def mark_visited(i, j):
    global visited_arr
    # 대각선 visited 처리
    di = [-1, -1, 1, 1]
    dj = [1, -1, -1, 1]
    flag_d = [True, True, True, True]

    visited_arr[i][j] = 1

    ccnt = 0
    k = 1
    while ccnt != 4:
        for d in range(4):
            if flag_d[d] is False:
                continue
            ni = i + di[d]*k
            nj = j + dj[d]*k

            # 정상인덱스일때만, 방문 표시
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                flag_d[d] = False
                ccnt += 1
                continue

            visited_arr[ni][nj] = 1

        k += 1
    # print(visited_arr)

def dfs(cnt):
    global visited_row, visited_col, visited_arr, flag, ans
    # 종료조건

    # 퀸을 N번 놓으면 종료
    if cnt == N:
        ans += 1
        return

    # 재귀
    # 놓을 수 있는 queen 위치 찾기
    for ii in range(N):
        if visited_row[ii]:
            continue
        for jj in range(N):
            if visited_col[jj] or visited_arr[ii][jj]:
                continue

            # 원복용 대각선 visited
            copied_arr = [[x for x in visited_arr[p]] for p in range(N)]

            visited_row[ii] = 1  # 행 visited 처리
            visited_col[jj] = 1  # 열 visited 처리
            mark_visited(ii, jj)
            dfs(cnt+1)

            # 원복
            visited_row[ii] = 0
            visited_col[jj] = 0
            visited_arr = copied_arr


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N 보드에 N개의 퀸을 서로 공격하지 못하게 놓는 경우의 수 세기

    ans = 0

    # print(visited)

    for i in range(N):
        for j in range(N):
            visited_arr = [[0]*N for _ in range(N)]     # 대각선 방문표시용 전체 배열 visited
            visited_row = [0] * N  # 행 visited
            visited_col = [0] * N  # 열 visited
            flag = 0

            # 처음에 놓을 퀸의 가로, 세로, 대각선방향 visited 표시
            visited_row[i] = 1  # 행 visited 처리
            visited_col[j] = 1  # 열 visited 처리
            mark_visited(i, j)
            dfs(1)

            # 원복안해도 초기화 된다. for로 도니까

    print(f'#{test_case} {ans}')