import sys
sys.stdin = open('input.txt', 'r')

'''
일꾼 수는 2명으로 고정.
결국 가로2칸으로 C내에서 최대인 값 찾기?
근데 문제에서 원하는 최대는 "제곱"들의 합이다.
N과 M이 작으니까 완전탐색으로 가능할 듯
단순히 최대인 영역을 찾는게 아니라
영역은 완전탐색으로 하고, 그 영역 내에서 조건에 맞는 꿀통 채취
2명이니까 현재 선택한 영역 제외하고 다른 곳에서 다른 사람 작업
근데 2명에 연연하지말고, 모든 영역을 다 본다음에, 
꿀채취값을 내림차순으로 2개 고르면 되지않을까?
dfs
영역은 왼->오로 측정
heapq 사용

인덱스 기준으로 "이 영역에서 채취할 수 있는 꿀의 최댓값 구하기"
하나의 값 고르는 순간 다른 못고르는 값들 생기므로 전부 다 따져봐야함
'''


def find_area_max(lst):
    # print(f'input_lst = {lst}')
    L = len(lst)
    max_v = 0
    for i in range(1<<L):       # 부분집합의 개수
        if i == 0:      # 공집합 제거
            continue
        temp_subset = []
        sum_temp = 0
        for j in range(L):      # 모집합의 길이만큼
            if i & (1<<j):      # i의 j번째 비트가 1인지 확인
                # 만약, 이 원소를 더해서 원소들의 합이 C를 넘는다면, break하고 다음 i로 넘어가기
                temp_subset.append(lst[j])
                sum_temp += lst[j]
                if sum_temp > C:
                    temp_subset = []
                    break
        # 원소들 제곱해서 더해보기
        sum_v = sum(map(lambda x:x**2, temp_subset))
        # 최댓값으로 업데이트
        max_v = max(max_v, sum_v)

    return max_v


def make_max_honey_lst():
    # max_honey_lst
    max_honey_lst = []

    # 인덱스 마다 가능한 최댓값 구하기
    for i in range(N):
        for j in range(N - (M - 1)):
            # 현재 인덱스 기준 영역들의 꿀 리스트 만들기
            honey_lst = arr[i][j:j + M]

            # 이 인덱스 기준에서 영역에서의 최댓값 구하기
            max_v = find_area_max(honey_lst)

            max_honey_lst.append((max_v, i, j))

    # 정렬
    max_honey_lst.sort(key=lambda x: x[0], reverse=True)  # 튜플의 첫번째 값을 기준으로 내림차순으로 정렬
    # print(max_honey_lst)

    return max_honey_lst


def solve():

    max_honey_lst = make_max_honey_lst()
    # print(max_honey_lst)
    L = len(max_honey_lst)
    max_vv = 0

    for p1 in range(L):      # 제일 큰 값([0])을 먼저 보고,
        for p2 in range(p1+1, L):      # 영역이 안 겹치는 선에서 두 번째로 큰 값 고르기
            p1_i, p1_j = max_honey_lst[p1][1], max_honey_lst[p1][2]
            p2_i, p2_j = max_honey_lst[p2][1], max_honey_lst[p2][2]

            if p1_i == p2_i and p1_j + M > p2_j:     # 영역이 겹친다면 pass
                continue

            # 영역이 안 겹친다면, 그때의 p1과 p2 인덱스의 max_v의 합이 최대
            temp_max = max_honey_lst[p1][0] + max_honey_lst[p2][0]
            # 최댓값 초기화
            max_vv = max(max_vv, temp_max)
            break

    return max_vv



T = int(input())

for test_case in range(1, 1+T):
    N, M, C = map(int, input().split())
    # N*N크기의 arr, 가로로 선택할 수 있는 벌통의 개수 M, 한 일꾼당 채취가능한 최대 양 C

    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve()

    print(f'#{test_case} {ans}')