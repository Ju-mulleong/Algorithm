import sys
sys.stdin = open('input.txt', 'r')

'''
미로에서 2를 출발점, 3을 도착점
1은 벽, 0은 길

DFS 활용
상하좌우 탐색 후 0으로만 들어가기
도달 가능 여부를 1 또는 0 으로 표시

'''


def find_start(arr):
    for ii in range(N):
        for jj in range(N):
            if arr[ii][jj] == 2:
                return ii, jj


def dfs(n, k, i, j):
    global ans
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # 가지치기
    if ans == 1:
        return



    # 기본 파트

    if arr[i][j] == 3:  # 도착점 찾으면 ans = 1
        ans = 1
        return


    # 유도 파트
    else:
        g = 1
        for d in range(4):
            ni = i + di[d]*g
            nj = j + dj[d]*g
            while 0 <= ni <= 15 and 0 <= nj <= 15 and arr[ni][nj] != 1:   # 정상인덱스고 벽이 아닐 때
                # 같은 방향으로 벽 나올때까지 계속 가보고, 벽 바로 앞의 위치로 이동

                g += 1
                ni = i + di[d] * g
                nj = j + dj[d] * g





                while arr[ni][nj] != 1:
                    dfs(n, k+1, ni, nj)
        return



T = int(input())

for test_case in range(1, 1+T):
    tc = int(input())

    N = 16
    # 16*16의 미로
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    i, j = find_start(arr)
    dfs(N ** 2, 0, i, j)

    print(f'#{test_case} {ans}')


