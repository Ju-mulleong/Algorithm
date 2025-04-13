import sys
sys.stdin = open('input.txt', 'r')
import heapq

# 방문 기록 (2차원)
visited = [[float('inf')] * N for _ in range(N)]
visited[s_i][s_j] = 0

while pq:
    cur_cnt, cur_i, cur_j, cur_k, cur_dir = heapq.heappop(pq)

    if visited[cur_i][cur_j] < cur_cnt:
        continue

    for d in range(4):
        ni = cur_i + di[d]
        nj = cur_j + dj[d]

        if not (0 <= ni < N and 0 <= nj < N):
            continue

        if arr[ni][nj] == 'T':
            if cur_k == 0:
                continue
            next_k = cur_k - 1
        else:
            next_k = cur_k

        # 방향 전환 커맨드 계산
        if cur_dir == d:
            n = 0
        elif cur_dir in (0, 3) and d in (0, 3):
            n = 1
        else:
            n = abs(cur_dir - d)

        next_cnt = cur_cnt + 1 + n

        # 방문 여부 판단 (커맨드 기준만으로)
        if visited[ni][nj] > next_cnt:
            visited[ni][nj] = next_cnt
            heapq.heappush(pq, (next_cnt, ni, nj, next_k, d))
