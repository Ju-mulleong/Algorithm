import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, 1+T) :    # test_case 별로 나눠서 처리

    N, M = map(int, input().split())    # 정수의 개수 N, 구간의 개수 M

    num = list(map(int, input().split()))   # N개의 정수들 num
    # N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산
    # 오름차순으로 재정렬한다음에 시작부분과 끝부분?
    for i in range(N-1, 0, -1):
        for j in range(i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    print(num)

    sum_of_num = 0
    # print(num[-0])
    # print(M)
    for m in range(M):  # 0, 1, 2, ... (M-1)
        # (num[-1] - num[0]) + (num[-2] - num[1]) ... (num[-m] + num[m-1])
        sum_of_num += num[-(m+1)] - num[m]
        print(sum_of_num)

    print(f'#{test_case} {sum_of_num}')
    # 출력값 틀림..
    # 문제조건과 다르다.
    pass
