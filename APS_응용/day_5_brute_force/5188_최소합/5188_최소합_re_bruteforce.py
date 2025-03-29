import sys
sys.stdin = open('input.txt', 'r')

'''
완전탐색으로 한다면, 최단거리니까 BFS 사용
'''


def dfs(node_i, node_j, sum_v):
    global min_v
    # 종료조건
    if node_i == N-1 and node_j == N-1:
        # 최솟값 업데이트
        min_v = min(min_v, sum_v)

    # 가지치기
    # 만약 이미 현재 시점 기준 최솟값보다 sum_v가 크거나 같다면, return
    if min_v <= sum_v:
        return

    # 재귀
    # 델타 적용한 방향으로 이동(우, 하)
    di = [0, 1]
    dj = [1, 0]

    for d in range(2):
        ni = node_i + di[d]
        nj = node_j + dj[d]

        # 정상인덱스일때만 실행
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue

        dfs(ni, nj, sum_v + arr[ni][nj])


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = float('inf')
    dfs(0, 0, arr[0][0])

    print(f'#{test_case} {min_v}')