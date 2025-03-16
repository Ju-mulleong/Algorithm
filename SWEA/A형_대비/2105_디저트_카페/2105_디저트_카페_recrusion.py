import sys
sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output.txt', 'w')
from collections import deque


'''
일단 중복 신경쓰지말고 d = 0, d = 1일때 최대 길이 각각 만들기
거기서부터 사각형 만들어가며 안되면 하나씩 빼기
'''

# d = 0, d = 1일때 최대 길이 찾기
def find_len(i, j, d):
    global memo, cnt_sum, max_v, s_i, s_j, cnt_0, cnt_1
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    ni = i + di[d]
    nj = j + dj[d]
    #
    # # 출발점으로 복귀했다면 지금까지의 cnt 최댓값 업데이트
    # if d == 3 and (ni, nj) == (s_i, s_j):
    #     cnt_sum += 1
    #     max_v = max(max_v, cnt_sum)
    #     return

    if d == 3:
        return cnt_0, cnt_1

    # 이 방향으로 가능한 한 계속 이동
    while 0 <= ni < N and 0 <= nj < N and memo[arr[ni][nj]] == 0:
        if d == 0:
            cnt_0 += 1
        elif d == 1:
            cnt_1 += 1
        # 이동
        memo[arr[ni][nj]] = 1
        ni += di[d]
        nj += dj[d]

    find_len(ni-di[d], nj-dj[d], d+1)


def make_max_v(i, j, cnt_0, cnt_1):
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    for ii in range(cnt_0):
        for jj in range(cnt_1):
            i + di[0]*ii
            j + dj[1]*jj



T = int(input())

for test_case in range(1, 1+T):
    N = int(input())    # N*N인 지역
    arr = [list(map(int, input().split())) for _ in range(N)]
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
            cnt_0 = 0
            cnt_1 = 0
            cnt_0, cnt_1 = find_len(i, j, 0)

            make_max_v(i, j, cnt_0, cnt_1)

    # 다 돌았는데 최댓값 업데이트 못했으면
    if max_v == 0:
        ans = -1
    else:
        ans = max_v

    print(f'#{test_case} {ans}')