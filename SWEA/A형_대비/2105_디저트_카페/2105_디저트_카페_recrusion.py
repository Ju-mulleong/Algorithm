import sys
sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output.txt', 'w')
from collections import deque


'''
일단 중복 신경쓰지말고 d = 0, d = 1일때 최대 길이 각각 만들기
거기서부터 사각형 만들어가며 안되면 하나씩 빼기
'''

# 최종
def move(i, j, d):
    global memo, cnt, max_v, flag
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    print(f'현재 칸 = {i, j} 값 = {arr[i][j]}')

    ni = i + di[d]
    nj = j + dj[d]


    if


    if 0 <= ni < N and 0 <= nj < N:
        if memo[arr[ni][nj]] == 0:
            memo[arr[ni][nj]] = 1


    else:
        return

    return







def do_it(i, j):
    s_i, s_j = i, j
    for d in range(4):
        move(d)

    # 다 돌아서 출발점으로 복귀했는가
    if s_i == i and s_j == j:
        return True


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
            flag = 0
            if do_it(i, j):
                max_v = max(max_v, cnt)

    # 다 돌았는데 최댓값 업데이트 못했으면
    if max_v == 0:
        ans = -1
    else:
        ans = max_v

    print(f'#{test_case} {ans}')