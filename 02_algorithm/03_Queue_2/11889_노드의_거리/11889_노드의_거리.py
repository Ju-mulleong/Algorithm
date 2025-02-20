import sys
sys.stdin = open('input.txt', 'r')

'''
시작 노드에서 최소 몇개의 간선을 지나면 도착 노드에 갈 수 있는가?
'''

def BFS(start, goal):
    # visited 생성
    visited = [0] * (V+1)       # 더미 포함 생성
    visited[start] = 1          # 출발점 방문

    # 출발점 append한 q만들기
    q = [start]

    # q가 빌때까지 실행
    while q:
        # deQueue하고 visited 수정

        dn = q.pop(0)
        # 만약 dn이 도착점이라면 지나온 간선 개수 반환
        if dn == goal:
            return visited[dn]-1    # 출발점 방문표시하기위해 1더했던거 지우기, 간선 개수 구하는 거니까
        # dn의 인접하고 미방문한 노드들 Q에 추가
        for j in adj_lst[dn]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = visited[dn]+1

    return 0


T = int(input())

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    # 노드와 간선 정보로 인접리스트 만들기
    adj_lst = [[] for _ in range(V+1)]    # 편의 위한 더미리스트를 0행에 추가(V+1)
    # print(adj_lst)

    for i in range(E):
        A, B = map(int, input().split())
        adj_lst[A].append(B)        # 1번행에 4번 노드 추가
        adj_lst[B].append(A)        # 4번행에 1번 노드 추가     # 방향성 없음!

    START, GOAL = map(int, input().split())
    # 출발노드 start, 도착노드 goal
    # print(adj_lst)

    print(f'#{test_case} {BFS(START, GOAL)}')
