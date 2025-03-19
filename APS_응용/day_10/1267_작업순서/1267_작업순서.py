import sys, pprint
from collections import deque
sys.stdin = open('input2.txt', 'r')


'''
인접 리스트로 저장하되, 부모들도 함께 저장?
위상정렬?, 진입차수
    Queue, dfs 둘 다 된다
'''


def bfs(dq):
    # print(node)
    global ans_lst, visited

    while dq:
        # deQueue
        node = dq.popleft()

        # 현재 노드의 부모가 있는지 확인
        # 부모가 있고, 방문안했으면 부모를 dq에 넣는다.
        if adj_lst[node][1]:
            for i in range(len(adj_lst[node][1])):
                if visited[adj_lst[node][1][i]] != 0:
                    continue
                dq.append(adj_lst[node][1][i])

        # 부모 없으면, 현재 노드 print한다.
        # visited도 체크
        if visited[node] == 0:
            print(f'{node}', end=" ")
            visited[node] = 1

        # 인접리스트에 있는 방문하지 않은 노드들 dq에 넣기
        for j in range(len(adj_lst[node][0])):
            if visited[adj_lst[node][0][j]] != 0:
                continue
            dq.append(adj_lst[node][0][j])


T = 10  # test_case 10개 고정

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    # V는 정점, E는 간선의 개수

    # 임시 input 받기
    temp_lst = list(map(int, input().split()))

    # 인접 리스트 만들기
    adj_lst = [[[], []] for _ in range(1+V)]  # 더미 0번 포함
    # print(adj_lst)

    # 출력할 ans_lst 만들기
    ans_lst = []

    # visited
    visited = [0]*(1+V)

    for i in range(E):
        p, c = temp_lst[i*2], temp_lst[i*2+1]
        # print(p, c)
        # 인접 저장
        adj_lst[p][0].append(c)

        # 부모 저장
        adj_lst[c][1].append(p)

    # print(adj_lst)

    dq = deque()
    dq.append(temp_lst[0])

    print(f'#{test_case}', end=" ")
    bfs(dq)
    print()
