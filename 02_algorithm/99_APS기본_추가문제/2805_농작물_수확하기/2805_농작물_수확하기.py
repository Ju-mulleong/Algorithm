import sys
import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())

'''
1. 이건 델타응용이 아니라 행 우선 탐색에서 
    행마다 특정 규칙대로 값을 더하는게 맞는듯?
    or
    이 행의 전체 합에서 특정 값만 빼기

둘 다 해보자

슬라이싱?
'''


def sum_lst(lst):
    sum_v = 0
    # pprint.pprint(lst)

    for i in lst:
        sum_v += i
    return sum_v


for test_case in range(1, 1+T):

    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    if N == 1:
        print(f'#{test_case} {arr[0][0]}')
        continue

    # pprint.pprint(arr)

    # N이 홀수니까 가운데 원소기준으로 양쪽으로 1칸씩 점점 늘리기
    # 그러다가 행의 길이와 구하는 값의 크기가 같아지면, 다시 역순으로 진행
    # 아니면 가운데 행에서 시작할 수 있을까?

    # arr[i][center]
    # arr[i+1][center-1:center+1+1:]

    center = (N//2)     # N = 5이면 2번 인덱스, 7이면 3번 인덱스, 9면 4번 인덱스...
    sum_arr = 0
    for i in range(N):
        if i <= center:     # 0, 1 ,2, 3
            k = i           # 0, 1, 2, 3
            sum_arr += sum_lst(arr[i][center-k:center+k+1:])

        else:        # 4, 5, 6
            k = (N-1)-i   # 2, 1, 0
            sum_arr += sum_lst(arr[i][center-k:center+k+1:])

    print(f'#{test_case} {sum_arr}')
