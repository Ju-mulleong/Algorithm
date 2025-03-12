import sys
sys.stdin = open('input.txt', 'r')

'''
[0, 0]에서 출발해서 [N-1, N-1]도착.
지나는 칸에 써진 숫자의 합계가 최소일때, 합계를 출력하라
BFS? DFS
'''


def dfs(i, j, sum_v):
    global min_v
    # 우랑 하만 간다.
    di = [0, 1]
    dj = [1, 0]

    # 가지치기
    if sum_v >= min_v:
        return

    # 종료조건
    if (i, j) == (N-1, N-1):
        # 끝칸에 도착하는 경우. 그때까지 최솟값 비교해서 업데이트
        if sum_v < min_v:
            min_v = sum_v
            return

    for d in range(2):       # d = 0: 오른 방향, 1:아래 방향
        ni = i + di[d]
        nj = j + dj[d]

        # 정상인덱스이면 이동
        if 0 <= ni < N and 0 <= nj < N:
            # print(ni, nj)

            # 재귀
            dfs(ni, nj, sum_v + arr[ni][nj])


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N칸

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 13*13*10        # N최대 13, 칸은 10이하의 자연수
    dfs(0, 0, arr[0][0])

    print(f'#{test_case} {min_v}')
