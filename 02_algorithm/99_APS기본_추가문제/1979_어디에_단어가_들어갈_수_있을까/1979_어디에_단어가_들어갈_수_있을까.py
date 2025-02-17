import sys
import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())

'''
단어의 길이가 딱 맞아야함!
일단 찾는 범위가 전부 1인가(단어를 쓸 수 있는 흰 칸인가)
가로방향으로 시작-1, 끝+1의 인덱스가 배열 밖이거나, 검은색 인덱스여야함.
세로방향도 마찬가지.
이것도 전치행렬로 재활용 되나?

흰색 부분이 1, 검은색 부분이 0

'''

def solve(arr):
    global cnt

    # 단어 가로로 자리 검색
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:  # 행 우선 탐색으로 값이 1일때만 탐색
                for k in range(K):  # 0, 1, 2
                    if 0 <= j + k <= N - 1:
                        if arr[i][j + k] != 1:  # 일단 흰 칸이 k칸만큼 연속되어서 단어를 쓸 수 있는가
                            break  # for k 나가기
                    else:
                        break  # for k 나가기

                else:  # 흰칸이 K만큼 연속되어있다면
                    # 일단 찾은 인덱스 양끝에 j-1, j+K+1이 배열의 범위 내인지 확인

                    if 0 <= j - 1 <= N - 1 and arr[i][j - 1] == 0:
                        # 단어 왼쪽 끝-1이 정상인덱스이고 0이라면
                        if j+K+1 >= N:      # 오른쪽+1칸이 비정상인덱스라면
                            cnt += 1
                        elif arr[i][j + K + 1] == 0:  # 오른쪽도 정상인덱스이고 0이라면
                            cnt += 1

                    elif j - 1 < 0:  # 단어 왼쪽 끝-1이 비정상인덱스라면
                        if j+K+1 >= N:
                            cnt += 1

                        elif arr[i][j + K + 1] == 0:  # 오른쪽도 정상인덱스이고 0이라면
                            cnt += 1

for test_case in range(1, 1+T):
    N, K = map(int, input().split())
    # N*N 크기의 배열, 단어의 길이 K

    cnt = 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint.pprint(arr)
    # arr은 N*N 크기의 배열

    solve(arr)
    arr = list(zip(*arr))     # arr전치행렬로 바꾸기
    solve(arr)

    print(f'#{test_case} {cnt}')