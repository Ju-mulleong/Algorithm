import sys
sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output.txt', 'w')


'''
2차원 배열을 대각선으로 순회..
사각형으로 다시 출발점으로 돌아와야 한다. 델타응용의 방향을 대각선으로 잡으면 될듯?
디저트를 가장 많이 먹을 수 있는 경로 찾기, 그 먹을 수 있는 디저트의 최댓값 출력
어떤 경우에도 디저트 못 먹을 경우 -1 출력

!! 카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안된다 !!

가지치기? 시작과 끝 열의 가게에서는 시작 불가능
    방향 특성상 반드시 시작점 기준으로 최소 2칸은 정상인덱스여야한다.
        즉, 끝 열과 끝-1열은 불가능

사각형이니까 d=0, d=3일 때의 k값과 d=1, d=4일때의 k값은 같아야한다.
일단 k = 1로 시작하고, 정상인덱스 벗어날때까지 증가,정상인덱스 까지의 값을 for 로 돌린다.

memo 활용

현재 인덱스에서 가장 큰 사각형만 보면된다.
출발점이 같은데 작은사각형은 의미없다. 무조건 종류 더 적음
'''


def solve(i, j):
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    # memo만들기
    memo = [0] * 101  # 인덱스 0은 더미
    memo[arr[i][j]] = 1
    # print(memo)
    origin_i = i
    origin_j = j
    print(f'origin_i = {origin_i}, origin_j = {origin_j}')

    cnt = 1
    ccnt = 0
    d = 0
    while d <= 3:
        print(f'i = {i + di[d]}')
        print(f'j = {j + dj[d]}')
        print(f'arr[i][j] = {arr[i][j]}')
        while True:
            # 그냥 무조건 이동했다고 생각하자
            ni = i + di[d]
            nj = j + dj[d]
            if ccnt == 2:
                if d in (0, 1):
                    d += 2
                else:
                    d -= 2

            if 0 <= ni < N and 0 <= nj < N:     # 정상인덱스인 경우
                # 정상적으로 돌아오는건 무조건 이거밖에 없음.
                if d == 3 and origin_i == ni and origin_j == nj and cnt >= 4:
                    return cnt

                if memo[arr[ni][nj]] == 0:  # 정상인덱스 인 경우, memo안된 디저트가게일 경우에만 이동
                    # 이동
                    i = ni
                    j = nj
                    memo[arr[i][j]] = 1
                    cnt += 1
                    print(f'이동 = {i, j}')
                    print(f'arr[i][j] = {arr[i][j]}')
                    print(f'cnt = {cnt}')

                # 정상인덱스이지만, 이미 갔던 가게인 경우
                # 뒤로 돌아가고(안움직였다 치고), 방향 바꾸기
                else:
                    ccnt += 1
                    break
            # 비정상인덱스인 경우
            # 뒤로 돌아가서 방향 바꾸기
            else:
                ccnt += 1
                break

        d += 1

    # 반복 다 끝났는데 만약 출발점으로 못 돌아왔다면, 디저트 못 먹은 것
    else:
        return -1


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())    # N*N인 지역
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_v = 0

    # 디저트 종류를 나타내는 수는 1이상 100이하

    for i in range(N-2):    # i는 끝 2열에서는 불가능    # 0, 1
        for j in range(1, N-1):     # j는 양 끝에서 불가능 # 1, 2
            max_v = max(max_v, solve(i, j))

    # 다 돌았는데 최댓값 업데이트 못했으면
    if max_v == 0:
        ans = -1
    else:
        ans = max_v

    print(f'#{test_case} {ans}')