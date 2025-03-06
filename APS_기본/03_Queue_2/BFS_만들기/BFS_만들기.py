import pprint

'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''


def bfs(s, V):  # 시작 정점 s, 마지막 정점 V
    visited = [0] * (V+1)   # visited 생성

    q = []                  # 큐 생성
    q.append(s)             # 시작점 enQueue
    visited[s] = 1          # 시작점 enQueue 표시
    while q:                # 큐가 비워질 때 까지 반복, front != rear
        t = q.pop(0)            # deQueue해서 t에 저장   만약 q.pop()이면 DFS가 되버린다.
        print(t)                # t정점에 대한 처리
        for w in adj_l[t]:      # t에 인접한 정점 w 중, 인큐되지 않은 정점이 있으면
            if visited[w] == 0:
                q.append(w)                     # enQueue하고, visited에 표시
                visited[w] = visited[t] + 1
                # 깊이를 visited에 저장 가능하도록, visited가 0이 아니라 본래의 기능인 방문확인도 가능하다.

    print(visited)


V, E = map(int, input().split())    # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접 리스트 ---------------------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):              # 간선 1개마다 노드 2개
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)        # 방향이 없는 경우
# 여기까지 인접리스트 --------------------------------
pprint.pprint(adj_l)
bfs(5, 7)
