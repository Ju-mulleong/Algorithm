import sys
sys.stdin = open('input2.txt', 'r')
# sys.stdout = open('output.txt', 'w')


'''
4방향 델타로 움직인다.
    최대까지 움직이고
    방향전환
    재귀    
'''


def solve(i, j, d):
    global memo, cnt, s_i, s_j, max_v
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    print(f'현재 칸 = {i, j} 값 = {arr[i][j]}')

    latest_v = [i, j]

    ni = i + di[d]
    nj = j + dj[d]

    # 만약, 방향 한번 돌렸는데도 이동 불가하면, 한 칸 뒤로 가기
    # 갈 수 있는 최대까지 이동
    while 0 <= ni < N and 0 <= nj < N:
        if [ni, nj] == latest_v:     # 방문했던 인덱스를 다시 방문하는 방향이라면 방향 복구하고 한 칸 뒤로 가면됨
            solve(ni, nj, (d+2)%4)

        if memo[arr[ni][nj]] == 0:
            print(f'이동한 값 = {arr[ni][nj]}')
            memo[arr[ni][nj]] = 1
            cnt += 1

            # 가장 최근에 방문한 인덱스 저장
            latest_v = [ni, nj]

            ni += di[d]
            nj += dj[d]

            k = 0

        elif d == 3 and ni == s_i and nj == s_j:    # 출발점으로 복귀
            max_v = max(max_v, cnt)
            print(f'최댓값 = {max_v}')
            return

        else:   # 목표값이 이미 중복된 경우, 방향 돌리기
            break

    # 방향 전환
    if d != 3:
        print(f'방향 전환 = {(d+1)%4}')
        solve(ni-di[d], nj-dj[d], (d+1)%4)


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())    # N*N인 지역
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_v = 0

    # 디저트 종류를 나타내는 수는 1이상 100이하

    for i in range(N-2):    # i는 끝 2열에서는 불가능    # 0, 1
        for j in range(1, N-1):     # j는 양 끝에서 불가능 # 1, 2
            # memo만들기
            memo = [0] * 101  # 인덱스 0은 더미
            memo[arr[i][j]] = 1
            cnt = 1
            s_i = i
            s_j = j
            solve(i, j, 0)

    # 다 돌았는데 최댓값 업데이트 못했으면
    if max_v == 0:
        ans = -1
    else:
        ans = max_v

    print(f'#{test_case} {ans}')