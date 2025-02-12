import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def is_sudoku(arr):
    # 각 탐색의 시행마다 조건 맞는지 확인, 조건 안맞으면 즉시 0 return

    # set의 길이로 하는 방법
    # 처음엔 행 우선탐색 하고, zip으로 전치행렬 만든뒤 열 우선 탐색 하기
    for _ in range(2):
        for i in range(9):
            if len(set(arr[i])) < 9:
                return 0

        arr = list(zip(*arr))

    # 격자 탐색
    # 한 행에서 격자 3번 탐색 후, 다음 행으로 넘어감
    lst = []
    d = 0
    f = 0
    while True:
        for i in range(d, 3+d):
            for j in range(f, 3+f):
                if arr[i][j] in lst:    # 중복 있으면 0 반환
                    return 0
                lst.append(arr[i][j])

        if f == 6:  # 마지막 행의 격자까지 탐색하면 행 초기화, 열 아래로 3 옮기기
            f = 0
            d += 3
        f += 3   # 한 격자 탐색하면 행방향으로 3 옮기기

        return 1    # 겹치는 숫자 아무것도 없으면 1 return


for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(9)]   # 9*9크기의 스도쿠
    # print(arr)

    print(f'#{tc} {is_sudoku(arr)}')

    # 같은 줄에서 1~9 하나씩 사용
    # 3*3 격자에서 또한 1~9 하나씩 사용
    #   이 때 격자는 항상 9칸, 위치 정해져있음

    # 행 우선 탐색, 열 우선 탐색 , 격자 탐색
    '''
    제약사항에서 arr의 input값은 모두 1~9사이의 정수이다. 
    조건에 안맞는 경우는
    1. 같은 수 중복해서 존재 (= 1~9 중 어떤 수가 빠져있음)
    밖에 없다.
    미리 빈 리스트 만들어놓고, 인덱스를 각각 1~9의 수라고 생각하자. (0~8)
    그 수 나올때마다 그 수의 인덱스에 해당하는 원소에 +1 한다.
    만약 이미 그 원소에 1이있다면(중복이라면) 0 return
        근데 그러면 그냥 한 행마다 or 한 열마다 set를 만들고 set의 길이 확인하면 되지않나?
        set는 중복 자동 제거되니까 중복인 값이 있었다면 길이가 9보다 짧을텐데
        행은 그냥 확인하고 열은 zip으로 전치해서 확인하면 되지 않나
    '''







'''
# 행 우선 탐색
    # for i in range(9):
    #     lst = [0] * 9   # 행 바뀔때마다 초기화 해줘야됨.
    #     for j in range(9):
    #         if arr[i][j] == 1:   # 만약 값이 있다면 (중복이라면) return 0
    #             return 0
    #
    #         lst[arr[i][j] - 1] = 1

# 열 우선 탐색
    # for i in range(9):
    #     lst = [0] * 9  # 열 바뀔때마다 초기화 해줘야됨.
    #     for j in range(9):
    #         if arr[j][i] == 1:  # 만약 값이 있다면 (중복이라면) return 0
    #             return 0
    #
    #         lst[arr[j][i] - 1] = 1
'''



