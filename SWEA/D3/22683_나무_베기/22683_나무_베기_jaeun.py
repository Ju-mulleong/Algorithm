import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def findstart(N, arr):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'X':
                return r, c

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def min_count(sr, sc, dir, tree_cnt, cnt):  # 시작, 방향, 나무횟수, 조작횟수
    # q = []
    q = deque()
    visited = set()
    # print(visited)
    q.append((sr, sc, dir, tree_cnt, cnt))
    visited.add((sr,sc, dir, tree_cnt))
    while q:
        r, c, dir, tree_cnt, cnt = q.popleft()

        if arr[r][c] == 'Y':    # Y 도착했으면
            return cnt

        # 전진
        nr = r + di[dir]
        nc = c + dj[dir]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 'G' or arr[nr][nc] == 'Y':
                state = (nr, nc, dir, tree_cnt)
                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, dir, tree_cnt, cnt+1))
            elif arr[nr][nc] == 'T' and tree_cnt > 0:
                state = (nr, nc, dir, tree_cnt-1)
                if state not in visited:
                    visited.add(state)
                    q.append((nr, nc, dir, tree_cnt-1, cnt + 1))

        # 좌회전
        new_dir = (dir+3) % 4
        state = (r, c, new_dir, tree_cnt)
        if state not in visited:
            visited.add(state)
            q.append((r, c, new_dir, tree_cnt, cnt+1))

        # 우회전
        new_dir = (dir + 1) % 4
        state = (r, c, new_dir, tree_cnt)
        if state not in visited:
            visited.add(state)
            q.append((r, c, new_dir, tree_cnt, cnt+1))

    return -1


# 최소 조작 횟수
# 4 방향으로 다 갈 수 있음. 나무 만나면 부시면 됨.
# 다만, 부수는 횟수가 정해짐
# 미로와 비슷하면서 RC카 문제를 활용해서 풀면 되지 않을까?
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    sr, sc = findstart(N, arr)      # 시작 점 찾기
    # print(sr, sc)       # 1 1
    ans = min_count(sr, sc, 0, K, 0)
    print(f'#{tc}', ans)



