import sys
import pprint
sys.stdin = open('input.txt', 'r')


def dfs_matrix(start):      # 출발점만 계속 바뀐다.
    visited[start] = 1      # 이게 visited를 V+1로 만든 이유?
    global ans
    for w in range(1, V+1):     # w in (1번, 2번... V번 노드)
        if adj_mat[start][w] == 1 and visited[w] == 0:  # start에서 w번 노드가 인접해있고, w번 노드 방문하지 않았을때
            # print(w)
            if w == goal:
                ans = 1
                # return 1은 안되는듯?

            dfs_matrix(w)

    # return None 생략되있다ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ


T = int(input())

for test_case in range(1, 1+T):
    ans = 0

    V, E = map(int, input().split())
    # V는 노드의 수
    # E는 경로의 수

    adj_mat = [list([0]*(V+1)) for _ in range(V+1)]   # 인접행렬 초기화
    # 편의를 위해 0번 노드 추가 (V+1)
    # pprint.pprint(adj_mat)
    visited = [0] * (V+1)       # 방문체크 초기화
    # 이것도 인덱스랑 노드번호 맞추기 위해 V+1로

    for i in range(E):
        s, e = map(int, input().split())
        adj_mat[s][e] = 1
        # adj_mat[s][e] = adj_mat[e][s] = 1     !!!!!!! 방향성이 없다면
    # pprint.pprint(adj_mat)

    start, goal = map(int, input().split())
    # print(start, goal)
    dfs_matrix(start)

    print(f'#{test_case} {ans}')