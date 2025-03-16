import sys, pprint
sys.stdin = open('input.txt', 'r')


'''
노드 N을 루트로 하는 서브트리에 속한 노드의 개수를 알아내기
순회 그냥 전위순회로
'''

def pre_order(node):
    global adj_lst, cnt

    if node:    # 존재하는 노드라면
        cnt += 1
        pre_order(adj_lst[node][0])
        pre_order(adj_lst[node][1])

T = int(input())

for test_case in range(1, 1+T):
    E, N = map(int, input().split())
    # E는 간선의 개수, N은 조건에서 서브트리의 루트
    input_lst = list(map(int, input().split()))
    # 노드 번호 쌍 주어진다. 노드번호 뒤죽박죽임
    # 크기고정된 인접리스트 사용
    adj_lst = [[0]*3 for _ in range(E+2)]   # 노드의 개수 +1, 더미 +1
    # print(adj_lst)
    # 인접리스트 왼쪽 자식, 오른쪽 자식, 부모 순서

    for i in range(E):
        p, c = input_lst[i*2], input_lst[i*2+1]

        if adj_lst[p][0] == 0:    # 왼쪽 자식
            adj_lst[p][0] = c

        else:   # 오른쪽 자식
            adj_lst[p][1] = c


    # pprint.pprint(adj_lst)
    # N을 루트로하는 서브트리에 속한 노드의 개수
    cnt = 0
    pre_order(N)

    print(f'#{test_case} {cnt}')