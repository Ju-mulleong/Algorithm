import sys, pprint
sys.stdin = open('input.txt', 'r')
import heapq

'''
가로/세로 따로 활주로 세면 됨.
for문 따로 만들기 귀찮으니까 배열 자체를 zip으로 전치행렬로 뒤집으면 된다.
 
경사로의 높이는 항상 1이고, 길이는 테케마다 주어진다.
경사로 지은 인덱스 소수로 바꿔버리기 (2 -> 2.5)
'''


# 이번 행에서 활주로 가능한지 판단
def is_can_slide(arr, i, lst):
    global cnt
    L = len(lst)
    copied_arr = [row[:] for row in arr]
    pprint.pprint(copied_arr)
    # nonlocal 사용하기 위해 중첩함수로 작성
    # 같은 연속된 값들의 끝 인덱스만 전달받기(또는 단일)
    # d가 +1 이면 우 확인, d가 -1이면 좌 확인

    def check(i, j, d):
        height = arr[i][j]
        print(copied_arr)
        print(f'i={i}, j={j}, d={d}')
        print(copied_arr[i][j+d])
        for x in range(X):
            # 비정상인덱스면 경사로 못지음
            if j+d < 0 or j+d >= N:
                return False

            # 다음 값이 현재 인덱스값보다 1 낮지 않으면, 경사로 못지음
            if copied_arr[i][j + d] != height - 1:
                return False
            # 활주로 지으면 음수로 바꿔서 표시.
            else:
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                copied_arr[i][j + d] = -(height - 1)
                print(copied_arr)

        return True
    # 값이 높은 인덱스부터 살펴본다.
    # 높은 값인 인덱스부터 처리하므로, 현재값보다 다음값이 높은 경우는 존재하지 않는다.

    # 단일인덱스거나, 연속된 인덱스의 양끝만 검사하도록
    modified_lst = []
    c = 0
    while c < L-1:
        print(f'c = {c}')
        print(lst)
        start = end = lst[c][1]
        print(f'start = {start}, end= {end}')
        print(lst[c])
        # 같은 높이가 연속된다면
        if lst[c][0] == lst[c+1][0] and abs(lst[c][1] - lst[c+1][1]) == 1:
            end = lst[c][1]
            start = lst[c+1][1]
            n = 1
            print(f'start = {start}, end= {end}')
            while c+1+n < L-2 and lst[c+1][0] == lst[c+1+n][0]:
                start = lst[c+1+n][1]
                n += 1
            c = c + n

        modified_lst.append((start, end))
        c += 1
        print(f'modified_lst = {modified_lst}')

    for cur in range(L):
        s, e = modified_lst[cur][0], modified_lst[cur][1]

        # 시작인덱스면 우만 확인, 끝인덱스면 좌만 확인
        if s == 0:
            if check(i, s, +1) is False:
                return
            continue
        elif e == N-1:
            if check(i, e, -1) is False:
                return
            continue

        # 행의 양 끝인덱스가 아닐 때
        else:
            if check(i, s, -1) is False or check(i, e, +1) is False:
                return
            continue

    # 전부 통과하면, 활주로 지은 것
    cnt += 1


def solve(arr):
    for i in range(N):
        # 값이 큰 인덱스부터 내림차순으로 행 다시 정렬
        lst = []
        for j in range(N):
            lst.append((arr[i][j], j))
        lst.sort(reverse=True)
        # print(lst)

        # 그냥 경사로 길이만큼 idx의 값 구해서 반복하여 비교?
        is_can_slide(arr, i, lst)


T = int(input())

for test_case in range(1, 1+T):
    # 지도의 한 변의 크기 N, 경사로의 길이 X
    N, X = map(int, input().split())

    # N*N 지형
    arr = [list(map(int, input().split())) for _ in range(N)]

    # arr의 전치행렬
    arr_zip = [list(row) for row in zip(*arr)]
    # pprint.pprint(arr)
    # pprint.pprint(arr_zip)

    cnt = 0
    solve(arr)
    solve(arr_zip)
    print(f'#{test_case} {cnt}')


