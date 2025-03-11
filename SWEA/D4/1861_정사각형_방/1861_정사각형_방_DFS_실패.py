import sys
sys.stdin = open('input.txt', 'r')


'''
arr[i][j] 에는 1이상 N^2 이하의 수 Aij가 적혀있고, 이 숫자는 모든 방에 대해 전부 다르다.
델타 상하좌우로 이동
    단, 목표 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야한다.
초기에 어떤 방에서 시작해야 가장 많은 개수의 방을 이동할 수 있는가?
DFS? 근데 N이 1 <= N <= 1000이다.
최악의 경우 재귀 1000번 해야할수도 있음.
BFS

출발해야하는 방 번호, 최대 방 방문수 출력
최대 방문수가 같은 초기번호가 여러개라면, 그 중 적힌 수가 가장 적은 수 출력

거꾸로 1씩 빼면서 새로운 시작점으로 조정할 수도 있나?
이미 지나간 경로 memoization?
'''

def dfs(i, j, s_i, s_j):
    global cnt, max_v, max_i, max_j, ans
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # 만약 memo에 목표 인덱스에 해당하는 칸의 값이 존재한다면, 그 값만큼 cnt에 더하고 return
    if memo[i][j]:
        cnt += memo[i][j] -1

    else:
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            # 정상인덱스이고, 현재 방보다 목표 방이 정확히 1 큰 경우에만 이동
            if 0 <= ni <= N-1 and 0 <= nj <= N-1 and arr[ni][nj] == arr[i][j] + 1:

                cnt += 1
                dfs(ni, nj, s_i, s_j)
                cnt -= 1    # 원상복구

    # 더 이상 갈 수 없으면, cnt 최댓값과 비교해서 업데이트
    if cnt > max_v:
        max_v = cnt
        ans = arr[s_i][s_j]
        max_i, max_j = s_i, s_j

    elif cnt == max_v:
        if arr[s_i][s_j] < arr[max_i][max_j]:
            ans = arr[s_i][s_j]
            max_i, max_j = s_i, s_j


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0]*N for _ in range(N)]
    max_v = 0
    ans = 0

    for i in range(N):
        for j in range(N):
            # 가지치기
            # 현재 칸에서 최대한 (주어진 배열내 원소의 최댓값)까지 1씩 계속 간다고 해도, 이미 나온 max_v값 못넘으면 dfs 실행하지 않기
            if N ** 2 - arr[i][j] < max_v - 1:
                continue
            cnt = 1
            dfs(i, j, i, j)
            # memo의 인덱스에 cnt 메모하기
            memo[i][j] = cnt

    print(f'#{test_case} {ans} {max_v}')

