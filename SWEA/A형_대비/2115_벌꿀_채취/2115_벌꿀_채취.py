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
'''


def make_subset(lst):
    print(f'input_lst = {lst}')
    L = len(lst)
    max_lst = []
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
        print(temp_subset)
        # 원소들 제곱해서 더해보기
        sum_v = sum(map(lambda x:x**2, temp_subset))
        # 최댓값 업데이트
        if len(max_lst) < 2:
            max_lst.append(sum_v)

        else:
            for mm in max_lst:
                if mm <
                    # 아 이거 하나 고르면 다른거 고를때 영향 줄수도 있겠다.. ㅅㅂ




def dfs(i, j):
    # 현재 인덱스 기준 영역들의 꿀 리스트 만들기
    honey_lst = []
    for jj in range(j, j + M):
        honey_lst.append(arr[i][jj])
    # print(honey_lst)

    # C에 걸러진 부분집합 만들기
    make_subset(honey_lst)





T = int(input())

for test_case in range(1, 1+T):
    N, M, C = map(int, input().split())
    # N*N크기의 arr, 가로로 선택할 수 있는 벌통의 개수 M, 한 일꾼당 채취가능한 최대 양 C

    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N-(M-1)):
            dfs(i, j)