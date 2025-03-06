import sys
sys.stdin = open('input.txt', 'r')


def dfs(v, adj_list):
    global ans
    visited[v] = 1  # 방문했으면 visited = 1로 바꿈.

    for i in adj_list[v]:
        if visited[i] == 0 :    # v에 인접하고 아직 안 간 정점이 있다면, 거기로 이동
            if i == 99:
                ans = 1         # 99에 닿을수 있다면 ans를 1로 바꿈.
            dfs(i, adj_list)

        else:      # 없다면, 돌아가기
            return 0

    pass


T = int(input())

for test_case in range(1, 1+T):
    E = int(input())    # 경로의 개수 E

    adj_input = list(map(int, input().split()))     # 인접한 노드의 순서쌍

    visited = list([0]*100)     # 방문확인 리스트 visited
    # print(visited)
    ans = 0     # 문제 답 출력위한 ans

    # 이번 문제는 0번 노드가 있다.
    # A번(0번)에서 B번(99번) 으로 갈 수 있는가를 1 or 0으로 출력

    # 단방향 인접리스트 adj_list 만들기
    adj_list = [[] for _ in range(100) ]    # 0~99니까 100개 만들어야함.
    # print(adj_list)

    for i in range(E):
        adj_list[adj_input[i*2]].append(adj_input[i*2+1])
        # print(adj_list)

    dfs(0, adj_list)
    print(f'#{test_case} {ans}')


