import sys
sys.stdin = open('input.txt', 'r')

'''
커맨드를 전부 실행 후, 목적지에 도달했는지를 확인해야함
    => 시뮬레이션
arr
G: 이동 가능한 땅
T: 이동 불가능한 나무
X: 현재 RC카의 위치
Y: 이동시키고자 하는 위치

command
A: 정상인덱스이고, 이동 가능할때만 이동
L: 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
R: 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전
'''


def find_start():
    # 출발점인 X만 구해도 된다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)
                return start


def solve(start, command, len_command):
    # 커맨드대로 실행
    start_i, start_j = start
    # 방향 우 상 좌 하 순서
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # 항상 위를 바라본채로 실행
    d = 1

    for i in range(len_command):
        # 앞으로 이동
        if command[i] == 'A':
            ni = start_i + di[d]
            nj = start_j + dj[d]
            # print(ni, nj)
            # 비정상인덱스인가?
            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue
            # 나무인가?
            if arr[ni][nj] == 'T':
                continue

            # 그 외(땅, 도착지, 출발점으로 돌아옴)
            start_i, start_j = ni, nj

        # 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
        elif command[i] == 'L':
            d = (d + 1) % 4

        # 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전
        elif command[i] == 'R':
            d = (d - 1)
            if d == -1:
                d = 3

    if arr[start_i][start_j] == 'Y':
        return 1
    return 0


T = int(input())

for test_case in range(1, 1+T):
    # 필드의 크기 N (N*N)
    N = int(input())

    arr = [list(input()) for _ in range(N)]

    start = find_start()

    # print(start, end)
    # 조종을 한 횟수 Q
    Q = int(input())

    ans = []
    # 커맨드의 길이, 커맨드
    for i in range(Q):
        len_command, command = input().split()
        len_command = int(len_command)
        command = list(command)
        ans.append(solve(start, command, len_command))

    print(f'#{test_case} {" ".join(map(str, ans))}')

'''
그렇다면, 네가 처음 제출했던 코드의 문제점은 바로 이 부분이야:

if arr[ni][nj] == 'Y':
    if i == len_command-1:
        return 1
        
이건 Y에 도달했을 때, 해당 명령이 마지막 명령일 경우에만 성공 처리하고 있어.
그래서 Y에 도달했다가 다시 움직이면 실패 처리돼버려

이미 도착점에 도착한 뒤, 마지막 커맨드가 회전일때도 당연히 1이다.
'''