import sys
sys.stdin = open('input.txt', 'r')


'''
상하좌우 한개씩 터진다.
    터트렸을때, 모든 꽃가루의 합 중 최댓값
'''


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N*M의 arr

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    max_v = 0
    for i in range(N):
        for j in range(M):
            k = arr[i][j]
            sum_v = k
            # 델타 설정
            for d in range(4):
                for kk in range(1, k+1):
                    ni = i + di[d]*kk
                    nj = j + dj[d]*kk

                    # 정상인덱스일때만 더하기
                    if 0 > ni or ni >= N or 0 > nj or nj >= M:
                        continue
                    sum_v += arr[ni][nj]

            # 최댓값 비교
            max_v = max(max_v, sum_v)

    print(f'#{test_case} {max_v}')