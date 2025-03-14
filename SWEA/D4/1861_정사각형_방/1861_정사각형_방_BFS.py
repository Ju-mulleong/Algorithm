import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


'''
arr[i][j] 에는 1이상 N^2 이하의 수 Aij가 적혀있고, 이 숫자는 모든 방에 대해 전부 다르다.
델타 상하좌우로 이동
    단, 목표 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야한다.
초기에 어떤 방에서 시작해야 가장 많은 개수의 방을 이동할 수 있는가?
DFS? 근데 N이 1<= N <= 1000이다.
최악의 경우 재귀 1000번 해야할수도 있음.
BFS

출발해야하는 방 번호, 최대 방 방문수 출력
최대 방문수가 같은 초기번호가 여러개라면, 그 중 적힌 수가 가장 적은 수 출력
'''

def bfs():
    global cnt, max_v, max_i, max_j, ans
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    while dq:
        # deQueue
        [i, j] = dq.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 정상인덱스이고, 현재 방보다 목표 방이 정확히 1 큰 경우에만 enQueue
            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1 and arr[ni][nj] == arr[i][j] + 1:
                cnt += 1
                dq.append([ni, nj])

def dfs(i, j, s_i, s_j):
    global cnt, max_v, max_i, max_j, ans
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        # 정상인덱스이고, 현재 방보다 목표 방이 정확히 1 큰 경우에만 이동
        if 0 <= ni <= N-1 and 0 <= nj <= N-1 and arr[ni][nj] == arr[i][j] + 1:
            cnt += 1
            dfs(ni, nj, s_i, s_j)
            cnt -= 1    # 원상복구

    # 더 이상 갈 수 없으면, cnt 최댓값과 비교
    if cnt > max_v:
        max_v = cnt
        ans = arr[s_i][s_j]
        max_i, max_j = s_i, s_j

    elif cnt == max_v:
        ans = min(arr[s_i][s_j], arr[max_i][max_j])

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    ans = 0
    dq = deque()

    for i in range(N):
        for j in range(N):
            dq.append([i, j])   # 초기 값 enQueue
            cnt = 1
            bfs()

    print(f'#{test_case} {ans} {max_v}')

