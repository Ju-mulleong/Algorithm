import sys
sys.stdin = open('input.txt', 'r')


def dfs(i, j, d, cnt):
    global visited, max_v
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    ni = i + di[d]
    nj = j + dj[d]

    if ni == s_i and nj == s_j:
        max_v = max(max_v, cnt)
        return

    # 정상인덱스이고, 미방문
    if 0 <= ni < N and 0 <= nj < N and visited[arr[ni][nj]] == 0:
        # 방문 표시
        visited[arr[ni][nj]] = 1

        # 같은 방향으로 계속 이동
        dfs(ni, nj, d, cnt + 1)

        # 막혀서 return하면, 방향 바꾸기
        if d < 3:
            dfs(ni, nj, d+1, cnt + 1)

        # 원복
        visited[arr[ni][nj]] = 0



T = int(input())

for test_case in range(1, 1+T):
    N = int(input())  # N*N인 지역
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0


    for i in range(N-2):    # i는 끝 2열에서는 불가능    # 0, 1
        for j in range(1, N-1):     # j는 양 끝에서 불가능 # 1, 2
            visited = [0] * 101  # 인덱스 0은 더미
            visited[arr[i][j]] = 1
            s_i = i
            s_j = j
            dfs(i, j, 0, 1)

    if max_v == 0:
        max_v = -1
    print(f'#{test_case} {max_v}')

'''
dfs형태를 그래프에 대입해서 잘 생각
return했을때 어떤 행동을 취해야 하는가?

배운 것 중에 생각하자. 
dfs, bfs, dp, greedy, ...
'''