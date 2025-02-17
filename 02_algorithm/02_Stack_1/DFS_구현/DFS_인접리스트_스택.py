'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(v, N):
    visited = [0] * (N+1)   # visited를 탐색 이후에도 써야되면 전역변수로 사용, 그렇지 않으면 지역변수해도 무방
    stack = []

    while True:
        if visited[v] == 0:     # 그 노드에 첫 방문이면
            visited[v] = 1
            print(v)

        for w in adj_lst[v]:  # v에 인접하고 방문을 안 한 w가 있으면
            if visited[w] == 0:
                stack.append(v)     # 현재 노드 push
                v = w   # w로 이동
                break

        else:
            if stack:           # pop
                v = stack.pop()

            else:       # 스택이 비어있으면
                break
        # 인접 노드 중 방문 안 한 w가 없는 경우





# 노드수, 간선수 받아야 함

# 노드수 변수명: V(Vertex, 정점)
# 간선수 변수명: E(Edge, 간선수)


V, E = map(int, input().split())
input_lst = list(map(int, input().split()))
adj_lst = [[] for _ in range(V+1)]

# i행에 i번 노드에 인접한 다른 노드번호 저장
# i*2, i*2+1로 하고 range(E)로 한다.
for i in range(E):
    v, w = input_lst[i*2], input_lst[i*2+1]
    adj_lst[v].append(w)
    adj_lst[w].append(v)    # 방향성 없을때!

dfs(1, V)


