import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):

    N = int(input())    # 배열의 크기 N
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 사냥꾼 = 1, 토끼 = 2, 바위 = 3   빈 칸 = 0
    # 총알 개수 무제한
    # 사냥꾼들의 총 잡은 토끼 수 출력

    # 1의 인덱스를 찾고, 거기서 8방향으로 델타 사용
    # 델타 진행중, 사냥꾼 나오면 그 방향 델타는 사용 안함.
    # 토끼 나오면 cnt += 1
    # 돌 나오면 그 방향 델타는 사용 안함

    # 평소처럼 한바퀴, 두 바퀴... 돌지말고
    # 한 방향 먼저 끝까지 해보고 다음 방향 해보는 식이 더 간결할듯?
    # while로 해야겠네

    # 델타 '우' 부터 시작해서 시계 반대방향으로 회전
    di = [0, -1, -1, -1, 0, 1, 1, 1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    cnt = 0

    for i in range(N):
        # print(f'i = {i}')
        for j in range(N):
            # print(f'j = {j}')
            if arr[i][j] == 1:      # 사냥꾼이면
                for d in range(8):
                    k = 1
                    while True:
                        ni = i + di[d] * k
                        nj = j + dj[d] * k

                        k += 1
                        # print(ni, nj)

                        if 0 <= ni <= N-1 and 0 <= nj <= N-1:   # 인덱스가 지도 내이면
                            if arr[ni][nj] == 1 or arr[ni][nj] == 3:    # 사냥꾼이나 돌이면
                                break

                            elif arr[ni][nj] == 2:    # 토끼이면
                                cnt += 1
                                # print(ni, nj,cnt)

                            else:           # 공백이면
                                pass

                            if not (0 <= i + di[d] * k <= N-1 and 0 <= j + dj[d] * k <= N-1):
                                # 다음 스텝이 지도를 넘어간다면 (k는 위에서 이미 더했다.)
                                break

                        else:   # 한 방향으로만 쭉 가므로 ni, nj가 지도를 벗어났다면 다음 방향으로
                            # rint("break",ni, nj)
                            break

    print(f'#{test_case} {cnt}')





