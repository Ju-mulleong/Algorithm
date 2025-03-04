import sys
sys.stdin = open('input.txt', 'r')


'''
2차원 배열을 대각선으로 순회..
사각형으로 다시 출발점으로 돌아와야 한다. 델타응용의 방향을 대각선으로 잡으면 될듯?
디저트를 가장 많이 먹을 수 있는 경로 찾기, 그 먹을 수 있는 디저트의 최댓값 출력
어떤 경우에도 디저트 못 먹을 경우 -1 출력

!! 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안된다 !!

가지치기? 시작과 끝 열의 가게에서는 시작 불가능
    방향 특성상 반드시 시작점 기준으로 최소 2칸은 정상인덱스여야한다.
        즉, 끝 열과 끝-1열은 불가능

사각형이니까 d=0, d=3일 때의 k값과 d=1, d=4일때의 k값은 같아야한다.
일단 k = 1로 시작하고, 정상인덱스 벗어날때까지 증가,정상인덱스 까지의 값을 for 로 돌린다.

그리고 디저트 가게 방문할 때마다 list에 추가한다. 만약, 리스트에 이미 그 숫자가 있다면, 
break로 다음 출발점 찾기
'''


def solve(i, j):
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]
    dessert_lst = [arr[i][j]]
    lst_k = []

    # 일단 현재 출발지점에서 가능한 제일 큰 사각형 만들기.
    # 그 사각형에서 변이 2 이상이면, 그 변 1씩 줄이면서 해보기
    for d in range(4):
        k = 1

        ni = i + di[d] * k
        nj = j + dj[d] * k

        while 0 <= ni <= N-1 and 0 <= nj <= N-1:  # 정상인덱스 인 경우에만

            if arr[ni][nj] in dessert_lst:  # 겹치는 디저트가 있으면 방향 틀기
                break

            # dessert_lst.append(arr[ni][nj])

            k += 1

        lst_k.append(k)




    # lst_k = [1, 2]

    # for first_k in range(1, lst_k[0]+1):
    #     ni = i + di[0]*first_k
    #     nj = j + dj[0]*first_k
    #
    #     dessert_lst.append(arr[ni][nj])
    #
    #     for second_k in range(1, lst_k[1]+1):
    #         ni = i + di[1] * second_k
    #         nj = j + dj[1] * second_k
    #
    #         dessert_lst.append(arr[ni][nj])
    #
    #
    #








T = int(input())

for test_case in range(1, 1+T):
    N = int(input())    # N*N인 지역
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_v = 0
    for i in range(N-2):
        for j in range(1, N-1):
            max_v = max(max_v, solve(i, j, 0))

    if max_v == 0:
        ans = -1
    else:
        ans = max_v

    print(f'#{test_case} {ans}')