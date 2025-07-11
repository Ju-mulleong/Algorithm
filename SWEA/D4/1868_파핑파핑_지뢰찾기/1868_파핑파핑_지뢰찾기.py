import sys
sys.stdin = open('input2.txt', 'r')
from pprint import pprint
from collections import deque

'''
지뢰찾기
클릭한 칸이 지뢰면 게임 끝,
지뢰가 아니라면 클릭 8방향에 있는 지뢰의 총 개수 표에 출력
    지뢰가 없다면, 0으로 표시하고 8방향에도 연쇄적으로 같은 동작수행(다시 8방향 탐색)
'*'가 지뢰, '.'는 그냥 땅
표의 크기와 표가 주어질 때, 지뢰가 있는 칸을 제외한 다른 모든 칸의 숫자들이 표시되려면
최소 몇 번의 클릭을 해야 하는가?

지뢰 클릭하면 끝나니까 지뢰는 피해야됨.
어차피 0 이 아니라면, 클릭한 칸 딱 하나만 숫자 표시됨.
    클릭했을때 어차피 (0이거나 / 0이 아니거나) 2가지 경우다. - 지뢰는 위치를 알고 있으므로 클릭하지 않는다.
    그렇다면, 0인 칸은 연쇄적으로 표시되니까 0을 우선적으로 다 터트려야됨.
최소가 아닌 경우: 0으로 터트릴수 있는 칸을 직접 눌러서 터트릴 때


cnt = 0
1. i, j 순회하여 본인 주위 8칸에 지뢰가 없으면 0으로 표시, 8방향 BFS, 숫자 표시하면 cnt += 1, 지뢰 있으면 cnt += 1

'''

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]


def bfs(i, j):
    global need_click
    dq = deque([(i, j)])

    # visited같은 느낌의 방문 표시, 0 연쇄로 터질때 중복해서 세지 않도록 표시
    arr[i][j] = -1

    while dq:
        i, j = deque.popleft(dq)

        # visited같은 느낌의 방문 표시, 0 연쇄로 터질때 중복해서 세지 않도록 표시
        arr[i][j] = -1

        # 내 주변으로 8방향 델타 확인
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            # 정상인덱스 체크
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue

            # 중복 체크
            if arr[ni][nj] == -1:
                continue

            # 이 방향의 칸이 0이라면, enQueue
            elif arr[ni][nj] == 0:
                dq.append((ni, nj))

            # 이 칸은 클릭 안해도 됨.
            need_click -= 1
            print((i, j), need_click)

            # visited같은 느낌의 방문 표시, 0 연쇄로 터질때 중복해서 세지 않도록 표시
            arr[ni][nj] = -1


T = int(input())

for test_case in range(1, 1+T):
    # N*N 크기의 표
    N = int(input())

    # 숫자 표시할 arr
    arr = [[0]*N for _ in range(N)]

    # 지뢰/숫자 표시하기
    # cnt_mine = 지뢰 수
    cnt_mine = 0
    for i in range(N):
        temp_lst = list(input())
        for j in range(N):
            if temp_lst[j] == '*':
                # 지뢰 표시
                arr[i][j] = '*'

                # cnt_mine 더하기
                cnt_mine += 1

                # 지뢰라면, 8방향으로 숫자 표시
                for d in range(8):
                    ni = i + di[d]
                    nj = j + dj[d]
                    # 정상인덱스 체크
                    if ni < 0 or ni >= N or nj < 0 or nj >= N:
                        continue
                    # 해당 방향 땅이 지뢰가 아니라면, 숫자 표시
                    if arr[ni][nj] != '*':
                        arr[ni][nj] = arr[ni][nj] + 1
    pprint(arr)


    # 만약 0이 존재하지 않는다면, 모든 지뢰가 아닌 칸들을 한 번씩 눌러야 답임.
    need_click = N*N - cnt_mine
    print(f'need_click = {need_click}')

    # 전체 순회해서 0인 칸 연쇄 작용 하도록
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                bfs(i, j)

    print(f'need_click = {need_click}')

    print(f'#{test_case} {need_click}')