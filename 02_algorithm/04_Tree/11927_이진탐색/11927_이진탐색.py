import sys
sys.stdin = open('input.txt', 'r')

'''
1부터 N까지의 자연수를 이진탐색트리로 저장하기
크기가 고정된 연결리스트 사용
'''

# 중위 순회
def in_order(n):
    global cnt

    if n <= N:
        in_order(n*2)
        cnt += 1
        nodes[n] = cnt
        in_order(n*2+1)


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 1부터 N까지 이진탐색트리 만들기
    # N은 노드의 개수이기도 하다.

    nodes = [0]*(1+N)

    # 중위순회로 만들기

    cnt = 0
    in_order(1)

    print(f'#{test_case} {nodes[1]} {nodes[N//2]}')