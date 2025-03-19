import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


'''
bfs, dfs 둘다 되나?
최단, 최소는 일단 bfs부터 생각
'''


def bfs(dq):
    global visited

    while dq:
        # 맨 앞에거 deQueue하기
        target_tuple = dq.popleft()
        target = target_tuple[0]
        cnt = target_tuple[1]

        # target이 M과 같으면 cnt return
        if target == M:
            return cnt

        # target에 연산들 적용해서 enQueue
        cal_lst = [target + 1, target - 1, target * 2, target - 10]

        for i in range(4):
            # 계산 결과가 방문했거나, 아예 조건에 맞는 수가 아니면 enQueue하지말기
            if cal_lst[i] < 1 or cal_lst[i] > 1000000 or visited[cal_lst[i]] != 0:
                continue

            dq.append((cal_lst[i], cnt + 1))
            visited[cal_lst[i]] = 1


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 시작 숫자, M은 목표 숫자

    # q에 시작 숫자 넣기
    dq = deque()
    dq.append((N, 0))

    # visited 생성, 수의 범위가 1 ~ 100,0000이다.
    visited = [0]*(1000001)
    ans = bfs(dq)

    print(f'#{test_case} {ans}')
