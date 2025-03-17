import sys
sys.stdin = open('input2.txt', 'r')


'''
그냥 순회하면 될거같은데
arr[0][1] + arr[1][0] , arr[0][2] + arr[2][0], ...
arr[1][2] + arr[2][1], ...
이건 N == 2일때, 
N/2개씩 나누어서 요리하는거다...

크기가 N/2인 부분집합 2개 종류 구하고, 그 하나의 부분집합마다 점수 계산

단, 한 재료를 쓰면 그 재료는 다시 사용할 수 없다
만약 (1, 2)를 사용하면, 그 다음 재료로 1, 2는 쓸 수 없다.

'''


# 식재료 집합의 시너지합 구하기
def sum_points(lst):
    # print(lst)
    sum_v = 0
    for i in range(len(lst)):
        # print(arr[lst[i][0]][lst[i][1]], arr[lst[i][1]][lst[i][0]])
        sum_v += (arr[lst[i][0]][lst[i][1]] + arr[lst[i][1]][lst[i][0]])  # 시너지합

    # print(sum_v)
    return sum_v


# 크기가 2인 부분집합 만들기
def make_subset2(main_set):
    # print(main_set)
    sub_set_lst2 = []
    NN = len(main_set)
    for i in range(1 << NN):
        sub_set2 = []
        for j in range(NN):
            if i & (1 << j):
                sub_set2.append(main_set[j])

        if len(sub_set2) == 2:
            sub_set_lst2.append(sub_set2)

    return sub_set_lst2


# 크기가 N/2인 부분집합들 만들기
def make_subset(main_set):
    global min_v
    sub_set_lst = []
    for i in range(1 << N):
        sub_set = []
        for j in range(N):
            if i & (1 << j):
                sub_set.append(main_set[j])

        if len(sub_set) == N//2:
            sub_set_lst.append(sub_set)

        # print(sub_set_lst)

    # 만들어진 N/2인 부분집합들 모은 리스트
    # 첫/끝, 첫+1/끝-1.. 짝짓기(중복 없는 짝)
    # 각각 그 식재료의 시너지들의 합 구하기
    for jj in range(len(sub_set_lst)//2):
        A, B = sub_set_lst[jj], sub_set_lst[-jj-1]
        A_subsets = make_subset2(A)
        B_subsets = make_subset2(B)

        sum_A = sum_points(A_subsets)
        sum_B = sum_points(B_subsets)

        # 시너지 차이 최솟값 비교 업데이트
        temp_v = abs(sum_A - sum_B)
        if temp_v < min_v:
            min_v = temp_v


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 0xffff

    make_subset(list(range(N)))

    print(f'#{test_case} {min_v}')