import sys
sys.stdin = open('input.txt', 'r')


def dfs(i):
    visited[i] = 1
    for k in adj_list[i]:
        if visited[k] == 0:
            dfs(k)


T = int(input())


for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 창용마을에 사는 사람의 수 = 노드
    # M은 서로를 알고 있는 사람의 관계 수 = 간선

    '''
    서로 아는 관계거나, 몇 사람을 거쳐서 알 수 있다면 하나의 무리로 취급한다.
    한 번의 DFS 탐색하고 return으로 최초 호출자리로 돌아올때마다 하나의 무리.
    '''

    # 양방향 인접 리스트, visited 생성
    adj_list = [[] for _ in range(N+1)]
    visited = [0]*(N+1)

    for i in range(M):
        V, E = map(int, input().split())
        adj_list[V].append(E)
        adj_list[E].append(V)

    # print(adj_list)
    # print(visited)
    cnt = 0
    for i in range(1, 1+N):     # 1, 2, 3... N
        if visited[i] == 0:     # 방문 안한곳만 dfs하게 해서 무리 중복해서 찾지 않도록
            dfs(i)
            # 갔다가 돌아오면 무리 하나
            cnt += 1

    print(f'#{test_case} {cnt}')


