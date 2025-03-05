import sys
sys.stdin = open('input.txt', 'r')


'''
자식+자식을 부모에 저장하고, 
부모 노드 번호 확인 부모 노드 번호 == L 이면 그 값 출력
후위순회로 한다.
    실행부분에서 자식들 값 더해서 해당 노드에 할당
'''

def post_order(n):
    if n <= N:
        post_order(n*2)         # 왼쪽 자식 탐색
        post_order(n*2+1)       # 오른쪽 자식 탐색
        # print(n)
        if tree[n] == 0:        # 왼쪽 자식만 있을 경우 생각해야도미
            if n*2 <= N:
                tree[n] += tree[n*2]
                if n*2+1 <= N:
                    tree[n] += tree[n*2+1]

T = int(input())

for test_case in range(1, 1+T):
    N, M, L = map(int, input().split())
    # 노드의 개수 N, 리프 노드의 개수 M, 출력해야되는 노드 번호 L

    tree = [0]*(N+1)
    for i in range(M):  # 리프 노드에 키값 할당
        a, b = map(int, input().split())
        tree[a] = b

    post_order(1)
    print(f'#{test_case} {tree[L]}')