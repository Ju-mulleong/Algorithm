import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # [i][j] = 2 일때, 터트리면 상하좌우로 2칸 터진다.

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v  = 0

    for i in range(N):
        for j in range(M):
            sum_v = arr[i][j]
            k = 1
            for d in range(4 * arr[i][j]):
                if d >= 4:
                    k = (d // 4) + 1
                d %= 4
                ni = i + di[d] * k
                nj = j + dj[d] * k

                if 0 <= ni <= N - 1 and 0 <= nj <= M - 1:
                    sum_v += arr[ni][nj]

            if sum_v > max_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')



