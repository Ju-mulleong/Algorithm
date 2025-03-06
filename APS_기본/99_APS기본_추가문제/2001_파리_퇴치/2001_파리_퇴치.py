import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # [i + M][j + M] 만큼 탐색

    max_v = 0
    for i in range(N):
        for j in range(N):
            sum_v = 0
            for di in range(M):
                for dj in range(M):
                    ni = i + di
                    nj = j + dj

                    if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                        sum_v += arr[ni][nj]

            if sum_v > max_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')