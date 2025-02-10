import sys
sys.stdin = open('input.txt', 'r')

T = 10      # 테스트 케이스 10개

# 일단 맨 마지막 행에서 x = 2인 인덱스 찾고 거기서 시작.
    # if로 1 위치 검사 상 좌 우
    # 일단 좌/우 에 1있는지 먼저 검사, 좌/우에 1있으면 상 검사 안해도 됨.
    # 좌/우에 1있으면 바로 델타 꺾기. 꺾은 뒤 상 나올때 까지 or 다음 index 0 나올때 까지 반복
    # 다시 상으로. 상이 default로 해야될듯

def find_starting_coordinate(arr):  # 0 또는 1로 이루어진 list arr을 매개변수로 받음
    # 시작 위치 찾기
    for j in range(len(arr[99])):
        if arr[99][j] == 2:  # int로 받았다.
            start = j   # 도착했던 index를 start에 할당

    # 만약 좌/우에 인덱스가 존재한다면
    # 존재 안하면 스킵
    # 좌/우에 1 있는지 검색하기

    # 검사하는걸 default로 잡고, start가 0이나 99면 break로 검색 안하기
    
    di, dj = 99, start
    flag = 'All'
    while True:    # 진행방향에 값이 있을 때 까지.
        right_value = 0     # 초기화, 좌/우에 값이 없어도 0
        left_value = 0
        # print(di)

        # 종료조건
        # 출발점 X 반환해야됨(출발점의 열 인덱스)

        if di == 0:
            return dj
        
        # 우 검사

        # 행 인덱스가 98이내에서만 실행
        if dj <= 98 and (flag == 'right_or_up' or flag == 'All'):
            right_value = arr[di][dj + 1]   # 우 값 검사

            # 우 값이 1이면 우로 이동
            if right_value == 1:
                # di = di         
                dj = dj + 1

                # 우로 갔으면 그 다음 시행에서는 좌 검사하면 안됨.
                flag = 'right_or_up'
                continue   # 아래 검사 안해도됨, 좌 값/ 우 값 둘 중 하나만 존재하며, 둘 중 하나라도 존재하면 상은 없다.


        # 좌 검사

        # 행 인덱스가 1이상에서만 실행
        if dj >= 1 and (flag == 'left_or_up' or flag == 'All'):
            left_value = arr[di][dj - 1]    # 좌 값 검사

            # 좌 값이 1이면 좌로 이동
            if left_value == 1:
                # di = di
                dj = dj - 1
                # 좌로 갔으면 그 다음 시행에서는 우 검사하면 안됨.
                flag = 'left_or_up'
                continue  

        # 좌 값/ 우 값 모두 없으면 당연히 상밖에 없다.

        # 좌/우값 없으면 상으로 이동
        if right_value == 0 and left_value == 0:    
            di = di - 1
            # dj = dj
            flag = 'All'
            continue


for test_case in range(1, 1+T):
    tc = int(input())   # 테스트 케이스의 번호 tc

    arr = [list(map(int, input().split())) for _ in range(100)]

    ans = find_starting_coordinate(arr)

    print(f'#{tc} {ans}')
