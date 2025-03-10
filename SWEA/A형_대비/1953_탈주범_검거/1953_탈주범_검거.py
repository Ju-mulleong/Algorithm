import sys, pprint
sys.stdin = open('input.txt', 'r')


'''
맨홀뚜껑이 시작부분, (start_i, start_j)
L이 탈출에 소요된 시간

"탈출한 지 1시간 뒤, 맨홀 뚜껑을 통해 arr에 진입"

1시간에 1칸간다. L시간이 경과했을때, 탈주범이 위치할 수 있는 장소의 개수
    즉 움직이는 모든 경우의 수에서 방문한 터널(칸)의 개수
    dfs
구조물 타입이 1,2,..7 정수로 주어진다. 딕셔너리?
정수에 따라 델타 값을 value로 준다.
방향은 우상좌하 평소대로하고, 델타의 인덱스를 정해주자
'''

dict_tunnel = {1: [0, 1, 2, 3], 2: [1, 3], 3: [0, 2], 4: [0, 1], 5: [0, 3], 6: [2, 3], 7: [1, 2]}


def dfs(c, l, i, j, visited):
    global ans_arr
    # 가지치기
    if c > l:
        return

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    # 현재 칸의 터널 종류
    d_lst = dict_tunnel[arr[i][j]]  # [0, 1, 2, 3]...

    for d in d_lst:
        ni = i + di[d]
        nj = j + dj[d]

        # 지금 터널 종류와 이동할 터널 종류가 서로 이어져서 통과 가능한가?
        # = 지금 칸과 이동할 칸의 차가 2인 d가 이동할 칸의 d에 포함되있는가
        if d >= 2:      # 2, 3
            nd = d-2    # 0, 1
        else:           # 0, 1
            nd = d+2    # 2, 3

        # 향하는 칸이 정상인덱스이고, 0이 아니고, 방문하지 않았고, 터널이 서로 이어져 있다면 이동하기
        if 0 <= ni <= N-1 and 0 <= nj <= M-1 and arr[ni][nj] and visited[ni][nj] == 0 and nd in dict_tunnel[arr[ni][nj]]:
            # 방문 표시
            visited[ni][nj] = 1
            dfs(c+1, l, ni, nj, visited)
            # 원복
            visited[ni][nj] = 0

        else:   # 갈수 있는 만큼 갔을때, ans_arr에 지금까지의 경로 표시
            for ii in range(N):
                for jj in range(M):
                    if visited[ii][jj] == 1:
                        ans_arr[ii][jj] = 1


T = int(input())

for test_case in range(1, 1+T):
    N, M, start_i, start_j, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint.pprint(arr)
    visited = [[0]*M for _ in range(N)]
    ans_arr = [[0]*M for _ in range(N)]
    visited[start_i][start_j] = 1
    # pprint.pprint(visited)

    dfs(1, L, start_i, start_j, visited)
    # pprint.pprint(ans_arr)
    # ans_arr에서 1 세기
    ans = 0
    for v in ans_arr:
        ans += v.count(1)

    # pprint.pprint(visited)
    print(f'#{test_case} {ans}')