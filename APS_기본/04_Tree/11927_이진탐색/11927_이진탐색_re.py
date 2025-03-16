import sys
sys.stdin = open('input.txt', 'r')


def in_order(node):
    global bst, num
    if node <= N:
        # 왼쪽 자식 방문
        in_order(node * 2)
        # 할 일
        bst[node] = num
        num += 1
        # 오른쪽 자식 방문
        in_order(node * 2 + 1)




T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 1부터 N까지의 자연수를 이진 탐색 트리에 저장

    # 이진 탐색 트리 만들기
    # 중위순회??
    bst = [0]*(1+N)     # binary search tree
    num = 1
    in_order(1)

    # 루트에 저장된 값, N//2번 노드에 저장된 값 구해서 출력

    print(f'#{test_case} {bst[1]} {bst[N//2]}')
