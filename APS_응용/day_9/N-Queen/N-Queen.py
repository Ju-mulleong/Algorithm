# 4*4 N-Queen 문제
# - (i, j) 좌표에 queen을 놓은 적이 있다.
# - visited 기록 방법
#   - 1. 이차원 배열
#   - 2. 일차원 배열로 효율적으로 하는 방법



# level: N개의 행에 모두 놓았다면, 성공! (조건에 따라 걸러내고, 가능한 경우만 다음행으로 진행할것이므로)
# branch: N개의 열
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가
    for i in range(row):
        if visited[i][col] == 1:
            return False

    # 2. 왼쪽 대각선?
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:    # 델타의 진행방향이 작아지기만 하니까, 0보다 큰지만 보면 된다.
        if visited[i][j]:
            return False

        i -= 1
        j -= 1

    # 3. 오른쪽 대각선?
    i, j = row - 1, col + 1
    while i >= 0 and j < N:  # 델타의 진행방향이 작아지기만 하니까, 0보다 큰지만 보면 된다.
        if visited[i][j]:
            return False

        i -= 1
        j += 1

    # 2번, 3번 따로 안쓰고 zip으로 묶어서 하나의 조건문으로도 가능능

    # 위의 3조건을모두 통과했다면
    return True

def dfs(row):
    global answer
    if row == N:    # 모두 놓으면 성공한 케이스
        answer += 1
        return

    # 후보군: N개의 열
    for col in range(N):
        # 만약 기존에 같은 열이나, 대각선에 놓았다면 못 놓는다!
        # 가지치기
        if check(row, col) is False:
            continue

        visited[row][col] = 1
        dfs(row + 1)
        visited[row][col] = 0   # 원복


N = 8
visited = [[0]*N for _ in range(N)]
answer = 0  # 가능한 정답 수

dfs(0)
print(answer)

'''
위의 방법은 visited를 이차원 배열로 하는 방법
일차원 배열로 하는 방법은?
    대각선방향은 기울기의 절댓값이 1이다.
    예를 들어, 현재 좌표가 (3, 7), 이전에 퀸을 놓은 좌표가 (1, 5)면
    |3 - 1| == |7 - 5| 이므로, False
    
    ??
    if abs(visited[row] - visited[col]) == abs(row - col):
        return False
'''