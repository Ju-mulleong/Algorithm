import sys
import pprint
sys.stdin = open('input.txt', 'r')



def is_omok(arr):     # 이차원 배열과 기준 위치 i, j 받음
    di = [0, -1, -1, -1, 0, 1, 1, 1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    # 한 방향씩 가보고 만약 그 방향의 다음 칸에도 돌이 있으면 그 방향으로 계속 탐색
    # 돌 있을때마다 cnt += 1. cnt == 5 되면 return "YES"
    # 이 방향에 돌이 더 이상없다면 다음방향 탐색, cnt 초기화

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    # 이 칸에 돌 있을때만 실행
                for d in range(8):
                    k = 1
                    cnt = 1
                    while True:
                        ni = i + di[d]*k
                        nj = j + dj[d]*k
                        if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                            if arr[ni][nj] == 'o':  # 다음 방향에 돌 있으면
                                cnt += 1
                                k += 1

                                if cnt == 5:
                                    return "YES"    # 오목이면 Yes 반환

                                continue    # k+=1하고 다음 while로 돌아감
                            else:   # 돌 없으면 다음 방향 탐색
                                break       # while break하고 다음 for d 로 이동

                        else:
                            break   # 이 방향 다음 인덱스 없으면 while break하고 다음 방향 탐색
            pass

    else:
        return "NO"     # for i 문 전부 마친다면 오목 없는 것, NO 반환



T = int(input())


for test_case in range(1, 1+T):
    N = int(input())

    arr = [list(input()) for _ in range(N)]
    # pprint.pprint(arr)

    # 가로, 세로, 대각선으로 5개 이상 연속한지 확인
    # 일단 행 우선 탐색하다가 돌 나오면 그 위치에서 가로, 세로, 대각선 검사
    # 5개 이상 있으면 바로 yes return
    # 없다면 continue
    # while이 나을듯?


    print(f'#{test_case} {is_omok(arr)}')

