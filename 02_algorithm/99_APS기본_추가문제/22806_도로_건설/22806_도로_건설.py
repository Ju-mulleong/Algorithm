import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가로 한 줄, 세로 한 줄로 도로 건설시 최소비용, 최소비용일 때 높이 구해서 출력
    # 최소 비용이 같은 경우가 둘 이상일 때는 낮은 높이로 도로를 건설한다.
    '''
    이차원배열 행 우선탐색으로 훑기
    각각 델타로 가로로 전부, 세로로 전부 훑음
    현재 값과 발견한 값과의 차를 구해서 각 시행마다 합산한다.
    시행마다 합산값과 (탐색값 중 최댓값) 기억해야함
    시행마다 합산값 최소이면 합산값, (탐색값 중 최댓값) 업데이트
    
    만약 시행 후 합산값과 최솟값 같으면, (탐색값 중 최댓값)을 비교하여 낮은 쪽을 기억한다.
    '''
    # 높이를 낮춰서 지을수도 있다

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    min_sum_of_diff = N**2 * 5   # 충분히 큰 값

    for i in range(N):
        for j in range(N):
            sum_of_diff = 0
            max_v = arr[i][j]
            for d in range(4 * N):   # 최악의 경우 N바퀴 돌아야함, 4*N번 시행
                k = 1 + d//4
                d = d % 4

                ni = i + di[d] * k
                nj = i + dj[d] * k

                if 0 <= ni <= N-1 and 0 <= nj <= N-1:   # 정상인덱스라면
                    # 차 구해서 합산
                    # 높이를 어디에 맞출 것인가?
                    # 만약 탐색원소들이 2,3으로만 이루어져있다면
                    # 2로 맞출때랑 3으로 맞출때 비교
                    # 최악의 경우 1,2,3,4,5가 전부 있다면 각각 전부 비교해야하나
                    # 이거 탐색한다음 딕셔너리에 넣자
                    # 리스트로하면 인덱스 +1이 해당값이라 치고, 5칸짜리 리스트 만들어서
                    # 값 나올때마다 해당하는 (인덱스 +1)에 1씩 더한다.






                    diff = abs(arr[i][j] - arr[ni][nj])
                    sum_of_diff += diff

                    # 탐색값중 최솟값 기억
                    if arr[ni][nj] < min_v:
                        min_v = arr[ni][nj]

            # 방향 탐색 전부 끝나면 sum_of_diff 비교
            if min_sum_of_diff > sum_of_diff:
                min_sum_of_diff = sum_of_diff





