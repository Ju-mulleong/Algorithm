import sys
sys.stdin = open('input.txt', 'r')

'''
[0, 0]에서 출발해서 [N-1, N-1]도착.
지나는 칸에 써진 숫자의 합계가 최소일때, 합계를 출력하라
BFS? DFS
'''


def dfs(i, j, sum_v):
    global min_v

    # 가지치기
    if sum_v >= min_v:
        return

    # 종료조건
    if (i, j) == (N-1, N-1):
        # 끝칸에 도착하는 경우. 그때까지 최솟값 비교해서 업데이트
        min_v = min(min_v, sum_v)
        return

    # 우랑 하만 간다.
    if j + 1 < N:
        dfs(i, j+1, sum_v + arr[i][j+1])

    if i + 1 < N:
        dfs(i+1, j, sum_v + arr[i+1][j])


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N칸

    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 0xffffff
    dfs(0, 0, arr[0][0])

    print(f'#{test_case} {min_v}')

'''
오프라인 강의
노드와 경로(간선)으로 이루어져있으므로 그래프이다.

for문이랑 if문 최대한 줄이자..
'''