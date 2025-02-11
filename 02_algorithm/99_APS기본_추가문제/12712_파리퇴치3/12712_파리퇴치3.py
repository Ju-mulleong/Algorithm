import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T


def kill_fly(di, dj):  # di, dj 는 델타값을 원소로 하는 리스트
    max_value = 0
    killed_fly = 0
    for i in range(N):
        for j in range(N):
            for d in range(4 * (N - 1)):
                d = d % 4
                ni = i + di[d]
                nj = j + dj[d]

            if 0 <= ni <= N - 1 and 0 <= nj <= N - 1:  # 델타 적용한게 정상 인덱스라면
                killed_fly += arr_fly[ni][nj]

            if killed_fly > max_value:
                max_value = killed_fly

    return max_value


for test_case in range(1, 1+T):
    N, M = map(int, input().split())

    arr_fly = [list(map(int, input().split())) for _ in range(N)]
    # print(arr_fly)

    # + 또는 x 모양으로 한 번 뿌려서 잡을 수 있는 최대 파리 수 구하기
    # 델타 응용 써야 될 듯.

    # 십자 모양
    # for로 모든 배열의 모든 원소 다 순회 한다.
    # 근데 자기랑 같은 열, 같은 행인 원소들 다 더하기
    # 델타 쓰자 안쓸라하다가 더 복잡해지는 것 같다
    # 우 하 좌 상 순서대로 d 돌리고 이 시행이 최대 4*(N-1) 번 실행된다.
    # 인덱스 정상일때만 합산

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_cross = kill_fly(di, dj)

    # X 모양
    # di, dj 새롭게
    # 이것도 십자랑 비슷한 순서로

    di = [-1, -1, 1, 1]
    dj = [1, -1, -1, 1]

    max_X = kill_fly(di, dj)

    if max_cross > max_X:
        print(f'#{test_case} {max_cross}')
    else:
        print(f'#{test_case} {max_X}')




