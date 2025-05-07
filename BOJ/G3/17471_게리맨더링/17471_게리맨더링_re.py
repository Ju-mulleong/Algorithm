import sys
sys.stdin = open('input4.txt', 'r')
from collections import deque

'''
N개의 구역을 2개의 선거구로 나눠야 함
가능한 모든 선거구 조합을 만들고, 연결되있는지 확인??

그래프
인접 리스트

만약 인접한 구역이 없다면, 섬이라는 뜻이므로 선거구는 반드시 섬과 섬이 아닌 값들로 이루어져야함 (또는 섬과 섬)


'''


def check_adj(lst):
    # BFS로 모든 노드 방문해보기
    visited = set()
    dq = deque()
    dq.append(lst[0])
    visited.add(lst[0])

    while dq:
        cur_n = dq.popleft()

        # 현재 노드의 인접 리스트 행
        for temp_n in adj_lst[cur_n]:
            # lst 안에 있으면서 아직 방문 안했다면,
            if temp_n in lst and temp_n not in visited:
                dq.append(temp_n)
                visited.add(temp_n)

    # visited의 길이와 lst의 길이가 같으면 인접한 것
    if len(visited) == len(lst):
        return True

    else:
        return False


def sum_popul(lst):
    sum_v = 0
    for n in lst:
        sum_v += population[n]
    return sum_v


N = int(input())

# 인구수 저장
population = [0]    # 더미
population.extend(list(map(int, input().split())))
# print(population)

# 전체 선거구 집합
field = list(range(1, N+1))
# print(field)

# 인접 리스트 만들기
adj_lst = [[]]

# 섬 리스트
island = []
for i in range(N):
    temp_lst = list(map(int, input().split()))[1::]
    adj_lst.append(temp_lst)


# print(adj_lst)
# print(adj_lst)

# 그룹 나누기(비트마스킹)

min_v = float('inf')
# print(island)
# print(field)

for i in range(1, (1 << N) // 2): # 2^N번 반복, i = 0 ~ 2^N-1
    lst_a = []
    lst_b = []
    for j in range(N):
        if (1 << j)&i:  # i의 j번째 비트가 1이라면
            lst_a.append(field[j])
        else:   # i의 j번째 비트가 0이라면
            lst_b.append(field[j])

        # 가지치기? 하는게 더 시간 먹나

    # print(f'lst_a = {lst_a}')
    # print(f'lst_b = {lst_b}')
    # print()

    # 선거구 나누는 조건: 각각의 선거구를 이루는 구역은 연결되있어함, 공집합 불가
    if lst_a and lst_b:     # 공집합 거르기
        # 연결 확인
        if check_adj(lst_a) is False or check_adj(lst_b) is False:
            continue

        # 통과했으면, 두 선거구 인구 차이의 최솟값 업데이트 시도
        min_v = min(min_v, abs(sum_popul(lst_a) - sum_popul(lst_b)))
        # print(f'min_v = {min_v}')

if min_v == float('inf'):
    min_v = -1

print(min_v)


