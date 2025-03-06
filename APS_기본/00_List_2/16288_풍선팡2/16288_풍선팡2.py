import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for test_case in range(1, 1+T):
    N, M = map(int, input().split())    # N x M 개 크기의 격자판

    # 격자판에서 상하좌우 네방향 탐색하여서 꽃가루 합 가장 큰 값 구하기.
    # 풍선 위치를 좌표로 표현하여 2차원 배열에 저장.

    arr = [[0]for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    print(arr)

    '''
        [   [2,1,1,2,2], 
            [2,2,1,2,2]...
        
        ]
        
    '''
    # 본인값 + 상하좌우 다 합한 것
    # 네방향탐색
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_value = 0

    for i in range(N):
        for j in range(M):
            sum_value = 0
            for d in range(4):
                if 0 <= i+di[d] < N and 0 <= j+dj[d] < M:
                    sum_value += arr[i + di[d]][j + dj[d]]
                    # print(sum_value)

            real_sum_value = sum_value + arr[i][j]  # 4 방향 꽃가루 다 더한거 + 자기 자신 꽃가루

            if real_sum_value > max_value:
                max_value = real_sum_value

    print(f'#{test_case} {max_value}')







