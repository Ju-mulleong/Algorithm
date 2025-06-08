import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1 + T):
    # 달팽이 숫자 N
    N = int(input())

    arr = list([-1] * N for _ in range(N))
    # print(arr)

    # 그냥 델타로 방향 전환해서 배열 채우기?
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i = 0
    j = 0
    d = 0
    for n in range(1, N*N+1):
        arr[i][j] = n
        # print(i, j, n)
        ni = i + di[d]
        nj = j + dj[d]

        # 정상인덱스 벗어나거나, 이미 숫자 작성되있으면 방향 바꾸기
        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != -1:
            d = (d+1)%4
            ni = i + di[d]
            nj = j + dj[d]
            # print(f'i: {i}, j: {j}')
        i = ni
        j = nj
        n += 1

    print(f'#{test_case}')
    for k in range(N):
        for ans in arr[k]:
            print(ans, end=' ')
        print()
