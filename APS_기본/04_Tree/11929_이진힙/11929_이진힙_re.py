import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 주어지는 키값의 개수 N

    # 이진 최소힙 만들기
    min_heap = [0]*(N+1)
    last = 0
    for i in map(int, input().split()):
        # 일단 입력받아서 제일 마지막 노드(last)에 넣는다.
        last += 1
        min_heap[last] = i

        # 넣었으면 기존 키값들과 비교해서 최소힙 유지하기

        # 현재 노드번호(자식)
        c = last

        # 부모 노드번호
        p = c//2

        # 만약 부모가 존재하고, 그게 자식(현재)보다 크다면, 위치 바꾸기
        while min_heap[p] and min_heap[p] > min_heap[c]:

            # 키값 바꾸기
            min_heap[p], min_heap[c] = min_heap[c], min_heap[p]

            # 다시 반복하기위해 조건 맞추기
            c = p
            p = c//2

    # print(min_heap)


    # 마지막 노드의 조상 노드들의 키 값 구하기
    # last 활용
    pp = last // 2
    sum_v = 0
    while min_heap[pp]:
        sum_v += min_heap[pp]
        pp //= 2

    print(f'#{test_case} {sum_v}')


