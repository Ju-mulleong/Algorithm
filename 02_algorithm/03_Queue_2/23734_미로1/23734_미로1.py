import sys
sys.stdin = open('input.txt', 'r')

'''
미로에서 2를 출발점, 3을 도착점
1은 벽, 0은 길

DFS 활용
상하좌우 탐색 후 0으로만 들어가기
도달 가능 여부를 1 또는 0 으로 표시

재귀로 들어가다가 앞에 벽이 있어서 막혔다면 return, 미로니까 정상인덱스가 아닌건 불가능하다 전부 벽에 둘러쌓임

출구에 도달 못한다는걸 어떻게 판단하나?
try-except?
계속 반복해서 출입 위치를 5번 방문하면?

'''


def find_start(arr):
    for ii in range(N):
        for jj in range(N):
            if arr[ii][jj] == 2:
                return ii, jj


def dfs(i, j):
    global ans
    global si, sj

    # 가지치기

    # 기본 파트

    if arr[i][j] == 3:  # 도착점 찾으면 ans = 1
        ans = 1
        return

    # 유도 파트
    else:
        for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:   # 미로니까 벽에 둘러쌓임, 1칸씩 델타한다면 전부 정상인덱스 내이다. 통로인지만 확인하면 됨.
                    visited[ni][nj] = 1
                    dfs(ni, nj)
                    # 갔다가 돌아오면 그 갔다왔던 방향 밴


        return




T = int(input())

for test_case in range(1, 1+T):
    tc = int(input())

    N = 16
    # 16*16의 미로
    arr = [list(map(int, input())) for _ in range(N)]
    cnt = 0
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    visited = [[0]*N for _ in range(N)]

    ans = 0
    # 시작 위치 구하기
    si, sj = find_start(arr)
    dfs(si, sj)

    print(f'#{test_case} {ans}')

'''
어차피 출구가 있다면 다시 '방문'하지 않는다.
찍고 돌아오는건 '방문'이아니다.
'''


