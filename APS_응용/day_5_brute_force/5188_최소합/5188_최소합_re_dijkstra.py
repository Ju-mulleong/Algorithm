import sys
sys.stdin = open('input.txt', 'r')
import heapq

'''
맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직이기
    이 때의 합계 출력
    다익스트라? 완전탐색?
'''


def dijkstra():
    # 오른쪽이나 아래로만 이동 가능
    # pq 생성
    pq = [(arr[0][0], (0, 0))]       # (누적 가중치, 인덱스)

    # 누적가중치 리스트 weight_lst 생성
    weight_lst = [[float('inf')]*N for _ in range(N)]
    # print(weight_lst)
    weight_lst[0][0] = arr[0][0]

    while pq:
        # heappop
        cur_weight, cur_idx = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        if cur_weight > weight_lst[cur_idx[0]][cur_idx[1]]:
            continue

        # 오른쪽, 아래 델타 설정
        di = [0, 1]
        dj = [1, 0]

        for d in range(2):
            ni = cur_idx[0] + di[d]
            nj = cur_idx[1] + dj[d]

            # 정상인덱스일때만 실행
            if 0 > ni or N <= ni or 0 > nj or N <= nj:
                continue

            # 새로운 가중치 만들기
            new_weight = arr[ni][nj] + cur_weight

            # 새로운 가중치가 weight_lst보다 크거나 같으면, pass
            if new_weight >= weight_lst[ni][nj]:
                continue

            # weight_lst 갱신
            weight_lst[ni][nj] = new_weight

            # enQueue
            heapq.heappush(pq, (new_weight, (ni, nj)))

    # print(weight_lst)
    return weight_lst[N-1][N-1]


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N*N 크기의 판

    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    print(f'#{test_case} {dijkstra()}')