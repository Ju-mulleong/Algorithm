import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트케이스의 개수 T

for tc in range(1, T + 1):  # 케이스별로 처리

    row = int(input())  # 방의 가로길이   # 9
    columns = list(map(int, input().split()))  # 각 상자들의 개수 # 7 4 2 0 0 6 0 7 0

    '''
    결국 낙차를 구해야 하는데, 
    이거 그냥 결국 빈칸만 세면 될거같은데 
    제일 column이 큰 줄 만큼 크기의 list를 만들고, 
    빈 칸을 전부 0으로 채운다음에 
    zip으로 묶어서 0 세면 되지않나

    '''
    # 제일 큰 상자높이 구하기
    max_column = columns[0]
    for column in columns:
        if column > max_column:
            max_column = column  # 7
    # print(max_column)

    box_list = [[] for _ in range(row)]
    # 각 column들을 1을 원소로 높이만큼의 수를 가지는 list로 만들어서 box_list에 저장
    for column_index in range(row):  # 0 1 2 3 4 5 6 7 8
        if columns[column_index] == 0:
            box_list[column_index] = []
        else:
            box_list[column_index] = [1] * columns[column_index]
        # [[1,1,1,1,1,1,1], [1,1,1,1], [1,1], [] ... ]
        # [[1],[1,1,1,1,...1]# 22개 ....]

    # print(f'box_list = {box_list}')

    # box_list의 원소들 전부 max_column의 크기를 가지는 list로 만들고, 빈 칸 0으로 채우기
    # .extend()로 0들 추가?

    for box in box_list:
        zero_cnt = max_column - len(box)
        if zero_cnt == 0:
            continue
        box.extend([0] * zero_cnt)
        # box_list = [[1,1,1,1,1,1,1], [1,1,1,1,0,0,0], [1,1,0,0,0,0,0], [0,0,0,0,0,0,0]...]
    # print(f'extended_box_list = {box_list}')

    # zip으로 회전이 완료됬을때 새 column들을 만들고, 0 개수 = 낙차 구하기

    zipped_rotate_box_list = list(map(list, zip(*box_list)))  # zip이 튜플로 묶는걸 list로 바꿈

    # print(f'zipped{zipped_rotate_box_list}')

    falling = []
    cnt = 0
    max_cnt = 0
    for rotate_box in zipped_rotate_box_list:
        # 박스 기준(= 1이라면) 자신보다 아래에 있는 빈 칸만 세어야 한다?
        # for이랑 슬라이싱으로 현재 인덱스 ~ 끝 인덱스를 슬라이싱하여 0 센다.
        # 현재 인덱스를 for로 하나씩 증가
        for i in range(len(rotate_box)):  # 0, 1, 2, 3, ..., 8
            if rotate_box[i] == 1:
                cnt = rotate_box[i:].count(0)
                if cnt > max_cnt:
                    max_cnt = cnt

    print(f'#{tc} {max_cnt}')

    pass