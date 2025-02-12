import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):

    N = int(input())    # 지형의 개수(열의 길이) N
    if N == 0:
        print(f'#{test_case} {0}')
        continue
    arr = list(map(int, input().split()))

    # 본인 기준 열 -1, 열 +1 의 값들과 비교하여 그 둘보다 크면 봉우리다.
    # 만약 시행했는데 봉우리일경우, 다음 열 봉우리 계산은 스킵(이미 자신보다 낮음)

    # 첫과 끝 인덱스 일 경우, 각각 오/왼만 비교하면됨.
    # N이 1일때랑 N이 2일때 좀 다름

    # 0 5 5 0 이면 봉우리 있는거다!!!!!

    cnt = 0
    flag = 0
    for i in range(N):
        if flag == 1:
            flag = 0
            continue

        if i == 0:
            if N == 1:
                cnt = 1
                break
            if arr[i+1] < arr[i]:
                cnt += 1
                flag = 1
                continue

        elif i == N-1:
            if arr[i-1] < arr[i]:
                cnt += 1
                flag = 1
                continue

        else:
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                cnt += 1
                flag = 1

    print(f'#{test_case} {cnt}')
