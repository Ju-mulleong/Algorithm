import sys
sys.stdin = open('input.txt', 'r')

T = 10      # 테스트 케이스 10개

for test_case in range(1, 1+T):
    tc = int(input())   # 테스트 케이스의 번호 tc

    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    # 일단 맨 마지막 행에서 x = 2인 인덱스 찾고 거기서 시작.
    # if로 1 위치 검사 상 좌 우
    # 일단 좌/우 에 1있는지 먼저 검사, 좌/우에 1있으면 상 검사 안해도 됨.
    # 좌/우에 1있으면 바로 델타 꺾기. 꺾은 뒤 상 나올때 까지 or 다음 index 0 나올때 까지 반복
    # 다시 상으로. 상이 default로 해야될듯

    # 시작 위치 찾기
    for j in range(len(arr[99])):
        if j == 2:  # int로 받았다.
            start = j   # 도착했던 index를 start에 할당

    # 만약 좌/우에 인덱스가 존재한다면
    # 존재 안하면 스킵
    # 좌/우에 1 있는지 검색하기

    # 검사하는걸 default로 잡고, start가 0이나 99면 break로 검색 안하기

    di, dj = 99, start
    while True:    # 진행방향에 값이 있을 때 까지.
        right_value = 0     # 초기화
        left_value = 0
        # 우 검사

        # 행 인덱스가 98이내에서만 실행
        if dj <= 98:
            right_value = arr[di][dj + 1]   # 우 값 검사

            # 우가 1이면 무조건 우로 간다.
            if right_value == 1:
                di = di
                dj = dj + 1
                break   # 아래 검사 안해도됨, 좌/우중 하나만 1. 좌/우 중 하나라도 1이면 무조건 좌/우 로 감.

        # 좌 검사

        # 행 인덱스가 1이상에서만 실행
        if dj >= 1:
            left_value = arr[di][dj - 1]    # 좌 값 검사

            # 좌가 1이면 무조건 좌로 간다.
            if right_value == 1:
                di = di
                dj = dj - 1
                break  # 아래 검사 안해도됨, 좌/우중 하나만 1. 좌/우 중 하나라도 1이면 무조건 좌/우 로 감.


        if left_value or right_value:   # 좌/우중 하나라도 1이라면 생각해보니까 둘 다 1일수는 없다.



        if arr[99][start + 1] == 1:
            pass


        # 기본은 상으로 움직이기 (도착-> 출발 역방향으로 추적)
        di = di - 1
        dj = dj





























print(f'#{tc} {ans}')