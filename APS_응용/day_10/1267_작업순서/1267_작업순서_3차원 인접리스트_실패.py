import sys, pprint
sys.stdin = open('input2.txt', 'r')


'''
인접 리스트로 저장하되, 부모들도 함께 저장?
4부터 시작
    1로 간다. 1의 부모가 4외에도 있는지 확인
        만약 있으면, 그 부모의 일부터 다시 다 처리한다(재귀)
'''


def dfs(node):
    # print(node)
    global ans_lst, visited

    # 현재 노드의 부모가 있는지 확인
    if adj_lst[node][1]:
        for i in range(len(adj_lst[node][1])):
            if visited[adj_lst[node][1][i]] != 0:
                continue
            dfs(adj_lst[node][1][i])
            if len(ans_lst) == V:
                return

    # 부모 없으면, 현재 노드 ans_list에 넣고, visited도 작성,
    ans_lst.append(node)
    visited[node] = 1

    # print(visited)

    # 인접리스트에 있는 방문하지 않은 노드들 방문
    for j in range(len(adj_lst[node][0])):
        if visited[adj_lst[node][0][j]] != 0:
            continue
        dfs(adj_lst[node][0][j])


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
    dfs(temp_lst[0])
    print(f'#{test_case} {" ".join(map(str, ans_lst))}')