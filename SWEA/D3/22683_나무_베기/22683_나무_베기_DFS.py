import sys
sys.stdin = open('input.txt', 'r')

'''
최소 리모컨 조작 횟수 구하기
필드
    G: 땅,
    T: 나무,
    X: 출발점
    Y: 목적지
항상 위를 바라본 상태로 시작
방향:
    우/상/좌/하 모두 1번의 커맨드로 변경 가능
    앞으로 이동/ 왼쪽으로 90도 회전 / 오른쪽으로 90도 회전
DFS
    일단 X에서 차를 완전탐색으로 움직인다. 
    만약 나무를 만나면 벨지 말지 선택한다.
    베었다면, K -= 1
    나무를 벨 수 있는 횟수이므로 K를 0으로 굳이 만들지 않아도 된다.
    모든 완전 탐색을 완료했을때, 가장 적은 커맨드의 숫자(시행횟수) 정답
'''

# 그냥 return으로 반복문 한꺼번에 나오고싶어서 함수로 씀
def find_start():
    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                return i, j


def dfs(s_i, s_j, s_d, cnt, cnt_k):
    # print(s_i, s_j, s_d, cnt, cnt_k)
    global min_v
    # 가지치기
    # 이미 최솟값보다 cnt가 크거나 같으면, return
    if cnt >= min_v:
        return

    # 종료조건
    if arr[s_i][s_j] == 'Y':
        # 최솟값과 cnt 비교
        min_v = min(min_v, cnt)
        return

    # 4방향으로 탐색
    for d in range(4):
        flag = False
        ni = s_i + di[d]
        nj = s_j + dj[d]
        # 비정상인덱스이거나, 방문했었다면 pass
        if 0 > ni or ni >= N or 0 > nj or nj >= N or visited[ni][nj]:
            continue

        # 만약 나무라면
        if arr[ni][nj] == 'T':
            # cnt_k가 K 미만이면, 나무 베기(cnt_k += 1 하고 이동) - 플래그로 표시
            if cnt_k < K:
                cnt_k += 1
                flag = True
            # 만약 cnt_k가 K와 같다면, 나무 못베므로 다른 방향
            elif cnt_k == K:
                continue

        # 시작할때 방향과 현재 방향이 다르다면 그만큼 커맨드 더 사용한 것(방향 전환(n) + 이동(1))
        if s_d != d:
            # 방문 표시
            visited[ni][nj] = 1

            # s_d와 d의 차이 구하기
            # 방향인덱스 경계값일때가 중점
            if d in (0, 3) and s_d in (0, 3):
                n = 1
            # 그 외는 그냥 빼서 절댓값
            else:
                n = abs(s_d - d)

            # 이동
            dfs(ni, nj, d, cnt+n+1, cnt_k)
            # 원복
            visited[ni][nj] = 0
            if flag:
                cnt_k -= 1

        # 같은 방향이었다면, 커맨드 1번 쓴거
        else:
            # 방문 표시
            visited[ni][nj] = 1
            # 이동
            dfs(ni, nj, d, cnt+1, cnt_k)
            # 원복
            visited[ni][nj] = 0
            if flag:
                cnt_k -= 1


T = int(input())

for test_case in range(1, 1+T):
    # N*N 필드의 크기 N, 나무를 벨 수 있는 횟수 K
    N, K = map(int, input().split())

    # 필드 arr
    arr = [list(input()) for _ in range(N)]
    # print(arr)

    # 출발점(i, j)
    s_i, s_j = find_start()

    # 델타 설정
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    # visited
    visited = [[0]*N for _ in range(N)]

    # 최솟값
    min_v = float('inf')

    # dfs
    dfs(s_i, s_j, 1, 0, 0)

    if min_v == float('inf'):
        min_v = -1

    # 출력
    print(f'#{test_case} {min_v}')
