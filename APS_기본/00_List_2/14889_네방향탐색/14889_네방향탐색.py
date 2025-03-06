import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) # 테스트케이스의 수 T

for test_case in range(1, 1+T):
    N = int(input())    # 배열의 크기 N

    # 2차원 배열 만들기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    # 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 '절댓값'을 구하시오.

    # 이웃한 방향 인덱스 계산 위해 방향 별로 델타 설정
    # 예를 들어, 왼쪽으로 한 칸은 행(i)는 안 변하고, 열(j)는 한 칸 더해야 한다
    # 미리 델타 설정안하고 for문 안에 for로 하나 더 만들어도 됨.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    sum_value = 0

    for i in range(N):
        for j in range(N):
            for d in range(len(di)):    # for di, dj in [[0,1], [1, 0], [0, -1], [-1, 0]]: 으로 해도 됨
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < N:   # index가 음수가 아니고, 배열의크기 N 안 넘어갈때 만 계산
                    diff = arr[ni][nj] - arr[i][j]
                    if diff > 0:
                        sum_value += diff
                    elif diff < 0:
                        sum_value += (-diff)

    print(f'#{test_case} {sum_value}')
