import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 델타값 세팅
    # 사실 x,y를 i,j보다 더 많이 쓴다고 하심
    # 근데 x가 행, y가 열 인것 주의
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 2차원 배열 순회
    sum_v = 0
    for i in range(N):
        for j in range(N):
            # 4방향 순회
            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]
                # 인덱스 체크
                if 0 <= ni < N and 0 <= nj < N:
                    diff = arr[i][j] - arr[ni][nj]
                    if diff > 0:
                        sum_v += diff
                    else:
                        sum_v += (-diff)

    print(f'#{test_case} {sum_v}')