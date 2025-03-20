import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


'''
위상정렬 사용해보자
BFS, Queue사용
진입차수(노드로 들어오는 간선의 수)가 0인 "모든" 노드를 enQueue하고 시작.
deQueue하고, 그 노드에 연결된 '간선'을 모두 제거한다.
그리고 새롭게 진입차수가 0이 된 노드를 enQueue한다.

인접리스트,
들어오는 간선의 개수(진입차수)를 저장할 일차원리스트,

처리할때 출력을 노드에 도착했을때 바로 하는것 or 리스트에 다 넣어놨다가 나중에 한꺼번에 출력하는거?
작업시간면에서는 전자가 나을거같고, 가독성 측면에서는 후자가 나을것같다
'''


def bfs(dq, incoming_lst):
    ans_lst = []
    while dq:
        # deQueue
        target = dq.popleft()

        # 처리 (append)
        ans_lst.append(target)

        # target에 연결된 간선 모두 제거
        for c in adj_lst[target]:
            incoming_lst[c] -= 1

            # 간선 제거로 인하여 새롭게 진입차수가 0이 된 노드 enQueue
            if incoming_lst[c] == 0:
                dq.append(c)

    return ans_lst


T = 10  # test_case 10개 고정

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    # V는 정점, E는 간선의 개수

    # 임시 input 받기
    temp_lst = list(map(int, input().split()))

    # 인접 리스트 만들기
    adj_lst = [[] for _ in range(1+V)]      # 더미 인덱스 0 포함

    # 진입차수 리스트 만들기
    incoming_lst = [0]*(1+V)

    # visited
    visited = [0]*(1+V)

    for i in range(E):
        p, c = temp_lst[i*2], temp_lst[i*2+1]

        # 인접 저장
        adj_lst[p].append(c)

        # 도착노드의 진입간선 + 1
        incoming_lst[c] += 1

    dq = deque()

    # 진입차수가 0인 모든 노드를 enQueue해야함
    for i in range(1, V+1):    # 1 ~ V
        if incoming_lst[i] == 0:
            dq.append(i)

    ans_lst = bfs(dq, incoming_lst)

    print(f'#{test_case} {" ".join(map(str, ans_lst))}')