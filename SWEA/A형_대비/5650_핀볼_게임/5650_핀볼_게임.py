import sys, pprint
sys.stdin = open('input.txt', 'r')


'''
출발점으로 돌아오거나, 블랙홀에 빠지기 전까지,
벽이나 블록의 수직/수평면에 최대한 많이 부딪히기
부딪힌다생각하지말고 그 칸에 도착했을때 특정 규칙에 따라 방향 바꾼다고 생각해도 무방
"방향이 반대로 바뀐다"는 결국 출발지로 돌아온다는 것
'''


def solve(i, j, d):
    global wormhole_lst
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    # 각 방향에 맞게 경사면인 블럭들 할당
    # 인덱스기준으로 방향을 (-1 해야되는 블럭, +1 해야되는 블럭)순으로 할당
    db = [(3, 4), (2, 3), (1, 2), (4, 1)]

    # 벽에 부딪힌 횟수
    cnt = 0

    # 처음 시작위치 저장
    start_i, start_j = i, j

    while True:
        # print(i, j)
        ni = i + di[d]
        nj = j + dj[d]

        # 정상인덱스 일때 실행
        if 0 <= ni < N and 0 <= nj < N:
            arr_v = arr[ni][nj]

            # 블랙홀, 처음 위치
            # 종료
            if arr_v == -1 or ni == start_i and nj == start_j:
                # print('블랙홀')
                return cnt

            # 0이면 그냥 지나가기
            elif arr_v == 0:
                i = ni
                j = nj
                continue

            # 블록의 경사면이면 방향 직각으로 꺾기
            elif arr_v in db[d]:
                if arr_v == db[d][0]:   # 방향 인덱스 -1
                    d = (d-1)
                    if d == -1:
                        d = 3
                else:
                    d = (d+1)%4
                i = ni
                j = nj
                cnt += 1
                continue

            # 웜홀
            elif 6 <= arr_v <= 10:
                i = wormhole_lst[arr_v][0] - ni
                j = wormhole_lst[arr_v][1] - nj
                continue

        # 방향 정반대로 바꾼다 == 시작 위치로 돌아온다 == 핀볼 종료
        # 블록의 수직/수평면방향 or 정상인덱스 밖일때
        cnt = cnt*2 + 1
        # print('출발점')
        return cnt


'''
완전탐색으로 점수의 최댓값 구하기
    벽이나 블록에 최대한 많이 부딪히기
방향 정 반대로 바뀌는 경우
    벽과 충돌, 블록의 수직/수평면 충돌

방향 직각으로 변경
    블록의 경사면

웜홀 만나면 같은 숫자의 다른 웜홀로 이동(진행방향 유지)

블랙홀 만나거나, 처음위치로 돌아오면 게임종료
    
출발위치와 진행방향은 임의 선정
    단, 블록, 웜홀, 블랙홀 있는 위치에서는 출발 불가
    
'''


T = int(input())

for test_case in range(1, 1+T):
    N = 
    N = int(input())
    # N*N 크기의 맵

    arr = [list(map(int, input().split())) for _ in range(N)]
    # -1은 블랙홀, 0은 빈 공간, 1~5는 블록, 6~10은 웜홀
    # 웜홀 짝 위치 알아야되니까 하나씩 순회하면서 위치 기록
    wormhole_lst = [[0, 0] for _ in range(11)]  # 그냥 6~10번 그대로 쓰고싶어서/ 나머지는 더미

    for i in range(N):
        for j in range(N):
            # 만약 arr[i][j]가 웜홀이라면, 짝 찾을수 있도록 기록
            w_num = arr[i][j]
            if 6 <= w_num <= 10:
                wormhole_lst[w_num][0] += i
                wormhole_lst[w_num][1] += j

    max_v = 0
    for i in range(N):
        for j in range(N):
            # 블록, 웜홀, 블랙홀이 있는 위치에서는 출발할 수 없다.
            # arr의 값이 0인 위치에서만 출발 가능
            if arr[i][j] != 0:
                continue
            # 진행방향 임의 설정
            for d in range(4):
                max_v = max(max_v, solve(i, j, d))

    print(f'#{test_case} {max_v}')