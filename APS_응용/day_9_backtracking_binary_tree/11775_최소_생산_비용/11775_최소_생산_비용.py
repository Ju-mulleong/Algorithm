import sys
sys.stdin = open('input.txt', 'r')


def dfs(row, sum_v):
    global visited, min_v
    # 종료조건
    if row == N:  # 마지막 행까지 왔으면, 최솟값 비교하여 업데이트
        min_v = min(min_v, sum_v)
        return

    # 가지치기
    # 이미 합이 지금 나와있는 최솟값보다 높거나 같으면, 가지치기
    if sum_v >= min_v:
        return

    # 이미 생산중인 공장은 제외
    for i in range(N):
        if visited[i]:
            continue
        # 생산중인 공장 아니라면, 생산
        visited[i] = 1
        dfs(row+1, sum_v + arr[row][i])
        visited[i] = 0  # 원복


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    min_v = 0xfffff

    dfs(0, 0)

    print(f'#{test_case} {min_v}')