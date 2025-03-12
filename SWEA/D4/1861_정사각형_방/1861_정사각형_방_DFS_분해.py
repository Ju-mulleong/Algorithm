import sys, pprint
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
'''

def move(i, j):
    global max_v, max_i, max_j, ans, memo
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    flag = 0
    cnt = 1
    ii = i
    jj = j

    while True:
        moved = False  # 이동 여부 확인위해 False로 저장, 이동하면 True로 바꾸기
        for d in range(4):
            ni, nj = ii + di[d], jj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[ii][jj] + 1:
                if memo[ni][nj] != 0:  # 메모이제이션 활용
                    cnt += memo[ni][nj]
                    flag = True
                    break
                cnt += 1
                ii, jj = ni, nj
                moved = True  # 이동했음을 표시
                break  # 이동했으면 다시 처음부터 탐색
        if flag or not moved:  # 더 이상 이동할 수 없으면 종료
            break

    # print("끝")
    # 더 이상 갈 수 없으면, cnt 최댓값과 비교
    if cnt > max_v:
        max_v = cnt
        ans = arr[i][j]
        max_i, max_j = i, j
        # print(f'최댓값:{max_v}')

    elif cnt == max_v:
        # print(arr[i][j], arr[max_i][max_j])
        if arr[i][j] < arr[max_i][max_j]:
            ans = arr[i][j]
            max_i, max_j = i, j

    # 탐색 시작한 위치에 이 위치에서 시작했을시 갈 수 있는 길이 표시
    memo[i][j] = cnt


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
            # 현재 칸에서 최대한 (주어진 배열내 원소의 최댓값)까지 1씩 계속 간다고 해도, 이미 나온 max_v값 못넘으면 move 실행하지 않기
            if N ** 2 - arr[i][j] < max_v - 1:
                # print(f'here, {i, j}')
                continue
            move(i, j)

    # pprint.pprint(memo)
    print(f'#{test_case} {ans} {max_v}')

