import sys
sys.stdin = open('input.txt', 'r')

'''
pij 는 0이상 100이하다. 곱해서 확률이 더 커질수는 없다
'''


def dfs(n, p):
    global visited, max_v
    # 종료조건
    if n == N:
        # 최댓값 비교
        # print(p)
        max_v = max(max_v, p)
        return

    # 가지치기
    # # 만약 0인 확률을 곱해서 0이되버렸다면, 더 이상 확률 늘릴수없다.
    # if p == 0:
    #     return
    # 아래 조건문 안에 포함

    # 만약 현재 확률이 최댓값보다 작다면, 최댓값에 도달할수없다. pij는 100이하임.
    if p <= max_v:
        return

    # # 만약 지금 행에서 최대인 확률을 곱했는데, 최댓값보다 작아진다면 return
    # if p*(max(arr[n])/100) < max_v:
    #     return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(n + 1, p * arr[n][i]/100)
        visited[i] = 0

    # for i in range(N):
    #     if visited[i] == 0:
    #         visited[i] = 1
    #         dfs(n + 1, p * arr[n][i]/100)
    #         visited[i] = 0
    #

    # 원래 아래코드로 해서 통과가 안됬었는데, continue쓰는 방식으로 하니까 그제서야 통과됬다.
    #     왜 continue가 더 빠른가?


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = -1
    visited = [0]*N

    dfs(0, 1)
    print(f'#{test_case} {max_v*100:.6f}')