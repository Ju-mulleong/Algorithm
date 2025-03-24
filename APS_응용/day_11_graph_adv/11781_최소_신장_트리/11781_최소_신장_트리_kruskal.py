import sys
sys.stdin = open('input.txt', 'r')


'''
kruskal
1. 모든 간선들을 가중치를 기준으로 오름차순으로 정렬
2. 작은 가중치인 간선들부터 선택한다.
    2.1 만약 사이클이 생기는 간선이라면, pass하고 다음 간선 본다
    
'''


def find_ref(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]

    return x


def union(node1, node2):
    ref_1 = find_ref(node1)
    ref_2 = find_ref(node2)

    # if ref_1 == ref_2:      # 싸이클 방지
    #     return            # 밑에서 싸이클 안돌때만 union 호출하니까 없어도 되긴함

    # 일정한 규칙으로 연결한다.
    # 더 작은 노드 번호를 대표자로
    if ref_1 < ref_2:
        parents[ref_2] = ref_1
    else:
        parents[ref_1] = ref_2


T = int(input())

for test_case in range(1, 1+T):
    V, E = map(int, input().split())
    # 0번부터 V까지 => 노드의 개수 = 1+V
    # E는 간선의 개수

    edges = []
    # 간선들 저장
    for _ in range(E):
        start, end, weight = map(int, input().split())
        edges.append((weight, start, end))
        # (가중치, 시작점, 도착점)순서대로 저장

    edges.sort()    # 가중치 기준 오름차순으로 정렬
    # print(edges)
    parents = [i for i in range(V+1)]     # make_set(노드를 기준으로 만들어준다.)

    # 작은 것부터 고르면서 나아간다.
    cnt = 0         # 현재까지 선택한 간선의 수
    sum_v = 0       # 가중치의 합

    for weight, start, end in edges:
        # start와 end가 연결이 안되어있으면 선택
        #  == 다른 집합이라면 연결
        if find_ref(start) != find_ref(end):
            union(start, end)
            cnt += 1
            sum_v += weight

            if cnt == V:    # MST 구성 완료
                break

    print(f'#{test_case} {sum_v}')