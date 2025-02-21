import sys
sys.stdin = open('input.txt', 'r')


'''
100일 중에서 치즈 덩어리가 가장 많을 때의 덩어리 개수를 구하시오.

x번째 날에는 맛있는 정도가 x인 칸을 먹어버린다.
갉아먹는건 계속 누적된다.
덩어리는 상하좌우로 안끊기고 계속 인접한 원소들을 한 덩어리로 취급
DFS? 근데 N이 100인데 
근데 visited를 2차원배열로 해서 만들면 될지도?

DFS로 arr을 돌리는데, 시작점도 찾아야한다. 시작점 찾는것도 함수로 해서 제일 처음 visited가 0인 곳에서 시작하도록
for i, for j 안에 DFS를 넣고, 한번 j 끝날때마다 덩어리 세기? 
'''


def dfs(i, j):
    global di, dj, visited, point

    # 가지치기

    # 일반 파트

    # 유도 파트
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni <= N-1 and 0 <= nj <= N-1 and visited[ni][nj] == 0 and arr[ni][nj] != -1:
            # 탐색한 인덱스가 정상인덱스이고 방문하지 않았고, 갉아먹지 않았다면
            visited[ni][nj] = 1
            # print(visited)
            dfs(ni, nj)


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())    # 치즈 한 변의 길이 N
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    max_cnt = 0
    max_point = 0

    for point in range(1, 100):
        cnt = 0
        if arr == [[-1] * N for _ in range(N)]:
            break
        # print(f'point: {point}')
        for i in range(N):
            for j in range(N):
                # 갉아먹은 칸은 -1로 바꾼다.
                if arr[i][j] == point:
                    arr[i][j] = -1
        # print(arr)

        for i in range(N):
            for j in range(N):
                if arr[i][j] != -1 and visited[i][j] == 0:
                    # 여기서 dfs 들어갈때마다 한 덩어리 생성된다.
                    dfs(i, j)
                    cnt += 1


        # 배열 다 돌면 최댓값 업데이트
        # print(cnt, max_cnt)
        max_cnt = max(cnt, max_cnt)

        visited = [[0]*N for _ in range(N)]     # visited 초기화

    print(f'#{test_case} {max_cnt}')