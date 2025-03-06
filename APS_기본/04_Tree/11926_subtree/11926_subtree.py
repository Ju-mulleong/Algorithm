import sys
sys.stdin = open('input.txt', 'r')


def pre_order(n):
    global cnt
    if n <= E+1 and n != 0:    # 인접리스트의 행의 인덱스의 최댓값이 노드의 개수이다.
        cnt += 1
        pre_order(tree[n][0])
        pre_order(tree[n][1])


T = int(input())

for test_case in range(1, 1+T):
    E, N = map(int, input().split())
    # E는 간선의 개수, N은 서브트리의 루트

    nodes = list(map(int, input().split()))
    # 노드 인풋 받기

    # 크기가 고정된 인접리스트 만들기
    tree = [[0]*3 for _ in range(E+2)]
    # print(tree)
    for i in range(E):
        p, c = nodes[i*2], nodes[i*2+1]

        if tree[p][0]:
            tree[p][1] = c
        else:
            tree[p][0] = c

        tree[c][2] = p

    # for i in tree:
    #     print(i)

    # 트리를 N부터 시작해서 전위순회로 cnt += 1
    cnt = 0
    pre_order(N)

    print(f'#{test_case} {cnt}')


