'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''


def dfs(v):
    # 시작정점을 방문체크, v V 다르다
    visited[v] = 1
    print(v, end=" ")
    # 시작정점(v)에 인접한 정점(w) 중에서 미방문한 정점을 다시 dfs()
    for w in range(1, V+1):
        if adj_mat[v][w] == 1 and visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())    # 정점수, 간선수
adj_mat = [[0]*(V+1) for _ in range(V+1)]   # 인접행렬 초기화
visited = [0] * (V+1)      # 방문체크
temp = list(map(int, input().split()))


for i in range(E):
    s, e = temp[2*i], temp[2*i+1]     # 위의 1 2 1 3 ... 저장
    adj_mat[s][e] = adj_mat[e][s] = 1  # 방향성이 없음

dfs(1)

