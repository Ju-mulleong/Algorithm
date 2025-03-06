import sys
sys.stdin = open('input.txt', 'r')

T = 10  # 테스트 케이스의 개수 10

for test_case in range(1, 1+T):

    tc = int(input())
    arr = []

    for i in range(100):    # 배열의 크기는 100 x 100
        arr.append(list(map(int, input().split())))
    # print(arr)

    # 행의 합, 열의 합, 대각선의 합 중 최댓값 구하기
    # 최댓값 변수 하나로 계속 업데이트 시키기
    max_value = 0

    # 행의 합 100개

    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        if sum_row > max_value:
            max_value = sum_row
        if i == 0:
            max_value = sum_row

    # 열의 합 100개

    for j in range(100):
        sum_column = 0
        for i in range(100):
            sum_column += arr[i][j]
        if sum_column > max_value:
            max_value = sum_column

    # 대각선의 합 2종류
    # 왼 -> 오, 오 -> 왼

    # 왼 -> 오
    # [0][0] + [1][1] + [2][2]... + [99][99]

    sum_diagonal_A = 0
    for i in range(100):
        sum_diagonal_A += arr[i][i]
        if sum_diagonal_A > max_value:
            max_value = sum_diagonal_A

    # 오 -> 왼
    # [0][99] + [1][98] + [2][97] ... + [99][0]

    sum_diagonal_B = 0
    for i in range(100):
        sum_diagonal_B += arr[i][99-i]
        if sum_diagonal_B > max_value:
            max_value = sum_diagonal_B

    print(f'#{tc} {max_value}')