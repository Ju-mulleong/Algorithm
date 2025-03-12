import sys, pprint
sys.stdin = open('input.txt', 'r')

def move(i, j):
    global max_v, max_i, max_j, ans, memo
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    flag = False
    cnt = 1
    ii, jj = i, j

    while True:
        moved = False  # 이동 여부 확인
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

    # 최대값 갱신
    if cnt > max_v:
        max_v = cnt
        ans = arr[i][j]
        max_i, max_j = i, j
    elif cnt == max_v:
        if arr[i][j] < arr[max_i][max_j]:  # 출발 번호 작은 것 선택
            ans = arr[i][j]
            max_i, max_j = i, j

    memo[i][j] = cnt  # 메모이제이션 저장


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