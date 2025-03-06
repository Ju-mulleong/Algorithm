import sys
sys.stdin = open('input.txt', 'r')


def sum_arr(arr):   # 2차원배열 arr 매개변수
    sum_v = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):    # 직사각형으로 자르니까 arr의 행의 길이는 모두 같다.
            sum_v += arr[i][j]

    return sum_v

def solve():
    for i in range(N):
        row_cutting1 = [list(cake[c]) for c in range(i + 1)]
        row_cutting2 = [list(cake[c]) for c in range(i + 1, N)]
        # print(row_cutting1)
        # print(row_cutting2)
        sum_r1 = sum_arr(row_cutting1)
        sum_r2 = sum_arr(row_cutting2)
        if sum_r1 == sum_r2 == (strawberry // 2):  # 되네?
            for j in range(N):
                column_cutting1 = [list(cake[c]) for c in range(j + 1)]
                column_cutting2 = [list(cake[c]) for c in range(j + 1, N)]
                sum_c1 = sum_arr(column_cutting1)
                sum_c2 = sum_arr(column_cutting2)
                if sum_c1 == sum_c2 == (strawberry // 2):
                    return 1

    else:
        return 0


T = int(input())

for test_case in range(1, 1+T):

    '''
    2차원 배열로 input받고, 모든 딸기 수 계산, 
    
    먼저 가로로 잘라서 2*obj_value 만들 수 있는지 확인.
        가능하다면 거기서 다시 세로로 잘라서 확인
    현재 이차원 배열안의 모든 원소를 더하는 함수 만들어서 
    경우마다 사용하면 될듯?
    '''
    N = int(input())    # N*N 크기의 케이크

    cake =[list(map(int, input().split())) for _ in range(N)]
    strawberry = sum_arr(cake)

    print(f'#{test_case} {solve()}')
