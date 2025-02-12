import sys
import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())

def is_omok(arr, i, j):     # 이차원 배열과 기준 위치 i, j 받음
    di = [0, -1, -1, -1, 0, 1, 1, 1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]





for test_case in range(1, 1+T):
    N = int(input())

    arr = [list(input()) for _ in range(N)]
    # pprint.pprint(arr)

    # 가로, 세로, 대각선으로 5개 이상 연속한지 확인
    # 일단 행 우선 탐색하다가 돌 나오면 그 위치에서 가로, 세로, 대각선 검사
    # 5개 이상 있으면 바로 yes return
    # 없다면 continue

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    # 돌이 있으면 가로, 세로, 대각선 검사
                # 함수 실행


