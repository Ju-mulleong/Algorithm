import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for test_case in range(1, 1+T):
    N = int(input())    # 달팽이의 크기 N

    # N행 N열의 이차원 배열
    # 달팽이껍질처럼 가야함 델타 응용 사용
    # 어차피 가는 방향은 4개 (상, 하, 좌, 우)
    # 처음엔 우로 진행하다가 인덱스 끝에 도달하면 하로 바꿈
    # 하에서도 끝에 도달하면 좌로,
    # 그 다음이 문제인데 좌에서 상으로 갈 때 인덱스 -1로 해야된다.
    # 이거 처음엔 0으로만 채워진 이차원 배열 만들고, 만약 그 값이 0이 아니라면(이미 정수를 넣었다면)
    # 거기서 멈춰서 방향 바꾸면 될듯

    # N행 N열의 0으로 이루어진 이차원 배열 만들기

    arr = [[0] * N for _ in range(N)]

    # 우 * N, 하 * N-1, 좌 * N-1, 상 * N-2... 의 순서대로 반복

    # [0][0] 부터 시작해서 N 만큼 좌로 이동하며 num 할당,   ([0][N-1]에 도착)
    # [1][N-1] 부터 시작해서 N-1만큼 하로 이동하며 num 할당 ([N-1][N-1]에 도착)
    # [N-1][N-1] 부터 시작해서 N-1만큼 좌로 이동하며 num 할당 ([N-1][0]에 도착)
    # [N-1][0] 부터 시작해서 N-2 만큼 상으로 이동하며 num 할당   ([1][0]에 도착)

    # [1][0] 부터 시작해서 N-2 만큼 좌로 이동하며 num 할당  ([1][N-2]에 도착)
    # .....

    delta_i = [0, 1, 0, -1]
    delta_j = [1, 0, -1, 0]

    num = 1

    ni = 0
    nj = 0
    arr[0][0] = 1

    for d in range((N ** 2) - 1):  # 첫 칸은 1로 채우고 시작하므로 최대 N**2-1번 반복
        if num == N**2:
            break

        d = d % 4
        # print(d)
        for _ in range(N):  # 최대 한 방향 당 N번 반복

            ni = ni + delta_i[d]    # 이동
            nj = nj + delta_j[d]    # 이동

            num += 1  # 숫자 +1

            arr[ni][nj] = num       # 숫자 칸에 할당
            # print(arr)

            # 끝 인덱스에 도착하거나, 다음 진행방향에 값 있으면 방향 바꾸기

            # 끝 인덱스에 도착하는건 처음 3번 방향 틀때 뿐
            if nj == N-1 and d == 0:
                # print('case1')
                break

            if ni == N-1 and d == 1:
                # print('case2')
                break

            if nj == 0 and d == 2:
                # print('case3')
                break

            if arr[ni + delta_i[d]][nj + delta_j[d]] != 0:
                # print('case4')
                break

    print(f'#{test_case}')
    for i in arr:
        print(" ".join(map(str, i)))  # arr의 각 원소배열들의 원소를 map으로 꺼내서 str로 변환시킨후 join으로 " "으로 연결




