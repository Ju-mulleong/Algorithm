import sys, pprint
sys.stdin = open('input.txt', 'r')


'''
벽돌에 숫자 적혀있다.
1은 그냥 돌, 다른 벽돌들은 구슬에 맞거나, 폭발에 맞으면
적힌 숫자 -1 만큼 상하좌우+본인 만큼 폭발한다.

폭발 처리
    맞은 지점 숫자 확인, 1이면 제거
    1제외 다른 숫자(n)이면 
        for i in range(1,n)
            ni = i + di[d]*k
            nj = j + dj[d]*k
    dfs로 일단 다 돌리면서 1번 끝날때 arr 업데이트?
    visited?
    남은 돌 개수 최댓값 업데이트
'''


# 중력 적용
def apply_gravity():
    global arr
    # 열 방향으로 arr 읽고, 벽돌들 사이의 0 제거하고 땡기기(한 열씩 반복)
    # 벽돌들 만날때마다 temp에 append한다.
    for j in range(W):
        temp = []
        for i in range(H):
            if arr[i][j] != 0:
                temp.append(arr[i][j])
        # 한 열에서 0행, 1행, 2행.. 순회
        # 천장(0행)에서부터 H-len(temp)번 만큼 0으로 바꾸고, 그 뒤로는 temp에서 순서대로 할당
        tt = 0
        for t in range(H):
            if t <= H-len(temp) - 1:     # t는 인덱스니까
                arr[t][j] = 0
            else:
                arr[t][j] = temp[tt]
                tt += 1


# 벽돌 터트리기
def dfs(i, j, score):
    global arr
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]

    k = arr[i][j]   # 벽돌의 값
    arr[i][j] = 0   # 본인 자리 0으로 터트림
    score += 1

    for kk in range(1, k):
        for d in range(4):      # (4방향을 한 칸씩 돌아가면서 탐색)을 k-1번 반복
            ni = i + di[d]*kk
            nj = j + dj[d]*kk

            # 위/아래 방향 0이면 그 방향으로는 벽돌 없다.(좌/우는 있을수도 있음) 근데 그거 if로 빼는것보다 그냥 안하는게 가독성이랑 복잡도측면에서 나을듯

            if 0 <= ni <= H-1 and 0 <= nj <= W-1:       # 정상 인덱스라면
                # 그냥 벽돌이라면
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    score += 1

                # 터지는 벽돌이라면
                elif arr[ni][nj] != 0:  # 1과 0 둘 다 아닐때
                    dfs(ni, nj, score)

    return score


# 구슬 쏘기
def shoot(n):
    global max_v, sum_v, arr, temp_arr

    print(n)
    if n == 0:  # 주어진 횟수만큼 다 했으면, 뿌신 벽돌개수 최댓값 업데이트
        pprint.pprint(temp_arr)
        max_v = max(max_v, sum_v)
        return
    # 선택한 열에서 아래로 쭉 내려서 가장 먼저 찾는 벽돌부터 시작 (0이 아닐때)
    for j in range(W):
        for i in range(H):
            if arr[i][j] != 0:
                temp_arr = arr          # 원복용 arr 저장
                print('원복용 temp_arr')
                pprint.pprint(temp_arr)
                temp_sum_v = sum_v      # 원복용 sum_v 저장

                now_score = dfs(i, j, 0)
                print(f'뿌수고 온 벽돌 개수: {now_score}')

                sum_v += now_score
                print(f'지금까지 뿌신 벽돌 개수: {sum_v}')

                apply_gravity()         # 다 터트렸으면 중력 적용
                print('중력 적용')
                pprint.pprint(arr)

                shoot(n-1)         # 중력 적용시키고 다시 shoot
                print('원복배열 temp_arr 확인')
                pprint.pprint(temp_arr)
                arr = temp_arr          # arr 원복(중력 원복)
                print('arr 원복')
                pprint.pprint(arr)

                sum_v = temp_sum_v      # sum_v 원복

                break        # 다음 열로 넘어가기


T = int(input())

for test_case in range(1, 1+T):
    N, W, H = map(int, input().split())
    # N은 구슬 발사 횟수, W가 폭, H가 높이인 벽돌들

    arr = [list(map(int, input().split())) for _ in range(H)]
    # print(arr)

    sum_v = 0
    max_v = 0
    temp_arr = []
    shoot(N)

    print(f'#{test_case} {max_v}')

