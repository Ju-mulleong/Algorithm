import sys
sys.stdin = open('input.txt', 'r')


'''
완전 이진 트리일때는 크기고정 인접리스트 굳이 ..?
'''

def post_order(node):
    if node <= N:
        post_order(node*2)
        post_order(node*2+1)
        if nodes[node] == 0:
            if node*2 == N:
                nodes[node] = nodes[node*2]
            else:
                nodes[node] = nodes[node*2] + nodes[node * 2 + 1]


'''
def post_order(n):
    if n <= N:
        if nodes[n]:    # 잎노드면 바로 리턴
            return nodes[n]
        else:           # 가지노드면 후위순회로 값 저장
            L = post_order(n*2)
            R = post_order(n*2+1)
            nodes[n] = L + R
            return nodes[n]
    
    else:   # 왼쪽 자식만 있을 때, 오른쪽 자식은 0 return
        return 0 
    이 마지막 else 헷갈릴 수도 있는데, 잎노드면 바로 return하고, 가지노드면 그때 후위순회한다는거에 집중
    첫번째 가지노드에서, 왼쪽만있다면 왼쪽은 무조건 잎노드,
    왼쪽 갔다가, 후위순회니까 오른쪽가는데 값이 없잖아? 그러니까 0 return하고
    부모노드는 이제 잎노드에서 받은값 + 0 하면 되는거
'''


T = int(input())

for test_case in range(1, 1+T):
    N, M, L = map(int, input().split())
    # N은 노드의 개수, M은 리프노드의 개수, L은 값을 출력할 노드 번호

    nodes = [0]*(N+1)   # 더미 포함, 인덱스가 각각 자신의 노드번호. 값 저장

    for i in range(M):
        idx, v = map(int, input().split())
        # idx는 리프노드번호, v는 리프노드의 값
        nodes[idx] = v

    post_order(1)
    # print(nodes)
    print(f'#{test_case} {nodes[L]}')

'''
완전 이진 트리면, 굳이 크기고정인접리스트 쓸 필요 없다.
'''