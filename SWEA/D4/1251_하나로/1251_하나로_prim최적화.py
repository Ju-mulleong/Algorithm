import sys
sys.stdin = open('input.txt', 'r')
import heapq
'''
모든 섬을 연결
환경부담금의 세율은 주어지니까, 
해저터널의 길이를 최소로 해야함. 
즉 최단경로로 모든 섬을 연결
MST(prim)
거리(가중치)는 현재 노드 기준으로 알 수 있을듯?
그냥 모든 섬이 다 인접해있다고 생각, 어차피 골라서 가는거니까
현재 노드에서 다른 모든 섬에 대한 거리 구하기,
그 중 최소인 섬으로 이동
반복?
'''

'''
prim 최적화
거리들 저장할 lst 만든다.
    lst는 인덱스에 더 작은 값으로 들어온다면, 업데이트
그리고 enQueue하기 전에, lst를 확인하고, 현재 가중치보다 lst 가중치가 작으면
enQueue자체를 안한다.
'''


def prim(start_idx):
    # visited
    visited = [0]*N

    # 최소 비용 저장 리스트
    dists = [float('inf')]* N
    dists[0] = 0

    # pq 만들기
    pq = [(0, start_idx)]

    sum_v = 0
    while pq:
        # deQueue
        cur_w, cur_idx = heapq.heappop(pq)

        # 이전에 넣어놨던 원소인데, 이미 최소가중치로 방문한 경우
        if visited[cur_idx]:
            continue

        # 방문 표시(간선 확정)
        visited[cur_idx] = 1
        sum_v += cur_w

        # 현재 섬 기준으로 다른 방문 안한 모든 섬들의 거리를 구해서 enQueue
        for t in range(N):
            if visited[t]:
                continue
            # 문제에서 환경부담금은 L**2 쓰니까 굳이 루트안해도 됨
            distance = (x_lst[cur_idx] - x_lst[t])**2 + (y_lst[cur_idx] - y_lst[t])**2

            # 우선순위 큐에 삽입된 거리를 저장하면서 진행
            # 더 작은 비용으로 갈 수 있을때만 heapq에 삽입
            if dists[t] > distance:
                dists[t] = distance
                heapq.heappush(pq, (distance, t))

    return sum_v


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N은 섬의 개수

    # 그냥 1_000_000짜리 arr 만들기?
    # 섬들의 x좌표, y좌표 주어진다.
    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())

    # 모든 섬이 전부 간선으로 이어져 있는 그래프라고 봐도 된다.
    # 미리 가중치 구하기..?

    # 하나의 인덱스 == 하나의 섬
    L_sqr = prim(0)

    print(f'#{test_case} {round(E*L_sqr)}')




