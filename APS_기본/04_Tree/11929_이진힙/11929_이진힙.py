import sys
sys.stdin = open('input.txt', 'r')

'''
입력받은 순서대로 추가
    조건에 맞게 힙 변경
    반복..
    
    크기고정된 인접리스트로 생성
'''

# 해당 n을 추가하고, 최소힙 조건만족할때까지 계속 반복
def push_heap(n):
    global last
    last += 1
    c = last

    heap[last] = n
    p = last//2
    # p는 부모 노드 번호, n은 자식 노드 키값, c는 자식 노드 번호

    while heap[p] > heap[c] and p != 0:     # 최소힙 불만족하고, 루트에 닿을때까지 반복한다.
        # 부모 자리와 자식 자리 바꾸기
        heap[p], heap[c] = heap[c], heap[p]

        # 그 다음 시행에서 자식노드에서 최솟값만 부모와 비교하도록
        c = p

        p = c//2


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 노드의 개수 N, N개의 서로 다른 자연수 주어진다.

    temp_lst = list(map(int, input().split()))  # 입력값 받기
    heap = [0] * (N+1)                          # 초기 힙 설정
    heap[1] = temp_lst[0]
    last = 1                                    # last

    # 입력값 받아서 최소힙으로 만들기
    for i in temp_lst[1::]:
        push_heap(i)

    # 마지막 노드의 조상 노드들 키값 합하기
    sum_v = 0
    while last:
        last = last//2
        sum_v += heap[last]

    print(f'#{test_case} {sum_v}')

'''
최소 힙은 부모가 자식들보다 작기만 하면 된다.
    새로 추가할때마다 형제노드와 비교해서 더 작은값 비교~~ 안해도 됨.
    새로 추가할때 형제가 있다면, 이미 그 형제는 부모보다 크다.
'''