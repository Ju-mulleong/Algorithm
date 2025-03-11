import sys, pprint
from collections import deque
sys.stdin = open('input.txt', 'r')


'''
BFS 사용해보기
현재 칸의 종류 확인 (deQueue)
    d를 종류에 따라 dict에서 선택한다.
    ni, nj 가 정해진다.
        ni, nj가 정상인덱스이고, visited하지 않았으며, 목표 칸도 현재 칸으로 입구가 열려있는 경우
        목표 칸의 visited를 현재 칸 +1로 할당한다.
        목표 칸을 enQueue한다.
'''

dict_tunnel = {0: [], 1: [0, 1, 2, 3], 2: [1, 3], 3: [0, 2], 4: [0, 1], 5: [0, 3], 6: [2, 3], 7: [1, 2]}

def bfs():
    global visited
    # 우, 상, 좌, 하
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    while dq:
        # deQueue
        [i, j] = dq.popleft()

        # 현재 칸에 해당하는 d 순회
        for d in dict_tunnel[arr[i][j]]:
            ni = i + di[d]
            nj = j + dj[d]

            if d <= 1:                  # d = 0, 1
                dd = d + 2              # dd = 2, 3
            else:                       # d = 2, 3
                dd = d - 2              # dd = 0, 1

            # 목표 칸이 정상인덱스이고,
            if 0 <= ni <= N-1 and 0 <= nj <= M-1:
                # 방문하지 않았으며
                if visited[ni][nj] == 0:

                    # 목표 칸이 현재 칸 방향으로 열려 있는가
                    if dd in dict_tunnel[arr[ni][nj]]:

                        # 현재 칸이 주어진 시간내에 갈 수 있는 최대 칸인가
                        if L != visited[i][j]:
                            # enQueue
                            dq.append([ni, nj])

                            # 방문 표시
                            visited[ni][nj] = visited[i][j] + 1


T = int(input())

for test_case in range(1, 1+T):
    N, M, start_i, start_j, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    dq = deque()
    dq.append([start_i, start_j])
    visited[start_i][start_j] = 1
    bfs()

    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 1:
                cnt += 1

    print(f'#{test_case} {cnt}')


'''
deque 쓸 때, .leftappend(), .append(), .leftpop(), .pop()

단, deque는 양 끝인덱스에서 추가와 제거에 효율적인 구조라서 중간 인덱스를 pop하는 기능은 없다.
이걸 유무로 deque쓸지 안 쓸지 구분해도 ㄱㅊ을듯.

보통 from collections import deque 못 쓰게 하는 문제는
n이 적어서 그냥 q로도 쉽게 가능한 경우..
'''