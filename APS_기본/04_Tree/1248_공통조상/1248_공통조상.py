import sys
sys.stdin = open('input.txt', 'r')

'''
두 개의 노드가 주어지면 그 노드들의 가장 가까운 공통조상 찾기
그리고 그 공통조상을 루트로 하는 서브트리 크기 출력

정점들 입력 받음
입력받은거 자리고정된 인접리스트로 만든다

공통부모 찾을때 그냥 함수 2번돌려도 되는데 두 노드에서 출발해서 동시에 찾으면 더 빨리 찾을수 있지 않을까?
'''

# 공통부모 찾기
def find_same_parents(t1, t2):
    # 현재노드가 다른 노드의 부모가 될 수 있으므로, 현재 칸도 1로 표시하고 시작
    adj_lst[t1][3] = 1
    adj_lst[t2][3] = 1
    while True:
        if t1 != 1:
            p1 = adj_lst[t1][2]

            # 만약 방문한 칸의 4번째 칸이 이미 1이라면, 그 부모가 공통부모
            if adj_lst[p1][3] == 1:
                return p1

            adj_lst[p1][3] = 1  # 방문한 부모 행에 4번째 칸을 1로 표시(visited)

            t1 = p1

        if t2 != 1:
            p2 = adj_lst[t2][2]

            # 만약 방문한 칸의 4번째 칸이 이미 1이라면, 그 부모가 공통부모
            if adj_lst[p2][3] == 1:
                return p2

            adj_lst[p2][3] = 1  # 방문한 부모 행에 4번째 칸을 1로 표시(visited)

            t2 = p2


# 매개변수로 받은 노드번호를 루트로 하는 서브트리의 크기 찾기
# 전위순회하면서 하나씩 카운트
def find_size_subtree(n):
    global cnt
    if n:
        cnt += 1
        find_size_subtree(adj_lst[n][0])    # 왼쪽 자식으로 이동
        find_size_subtree(adj_lst[n][1])    # 오른 자식으로 이동


T = int(input())

for test_case in range(1, 1+T):
    V, E, target1, target2 = map(int, input().split())
    # V는 정점의 개수, E는 간선의 개수, target1과 target2 노드의 공통조상 찾기
    nodes_lst = list(map(int, input().split()))

    adj_lst = [[0]*4 for _ in range(V+1)]   # 조상 찾기 쉽게 하기위해 한 칸(visited) 더 만들기

    for i in range(E):      # 자리고정 인접리스트 만들기
        p, c = nodes_lst[i*2], nodes_lst[i*2+1]

        if adj_lst[p][0]:
            adj_lst[p][1] = c
        else:
            adj_lst[p][0] = c

        adj_lst[c][2] = p
    # print(adj_lst)

    # target1, target2의 공통조상 찾기
    same_p = find_same_parents(target1, target2)

    cnt = 0
    find_size_subtree(same_p)

    print(f'#{test_case} {same_p} {cnt}')