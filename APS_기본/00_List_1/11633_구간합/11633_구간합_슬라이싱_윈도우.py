import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, 1+T) :    # test_case 별로 나눠서 처리

    N, M = map(int, input().split())    # 정수의 개수 N, 구간의 개수 M

    num = list(map(int, input().split()))   # N개의 정수들 num
    # N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
    # M개의 합이 가장 큰경우와 가장 작은 경우의 차이 출력

    # 일단 M개의 이웃한 값 계산 식 작성하고 반복하여 최대/최소 업데이트
    # 전부 계산하면 몇 번 해야하는가?

    for i in range(N-(M-1)):
        sum_num = 0
        for j in range(M):
            sum_num += num[j+i]
        # sum_num = num[i] + num[i+1] + num[i+2]... +  num[M-1]

        if i == 0:
            max_sum = sum_num
            min_sum = sum_num
            # 초기 배열 합 최대/최소 로 지정
        if sum_num > max_sum:
            max_sum = sum_num

        if sum_num < min_sum:
            min_sum = sum_num

    print(f'#{test_case} {max_sum-min_sum}')
    pass
