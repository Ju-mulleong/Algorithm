import sys
import pprint
sys.stdin = open('input.txt', 'r')


def find_tank():
    for ii in range(H):
        for jj in range(W):
            if battle_field[ii][jj] in '>^<v':
                return ii, jj


T = int(input())    # 테스크 케이스의 개수 T

for test_case in range(1, 1+T):
    H, W = map(int, input().split())
    # 게임 맵은 H*W 크기의 격자판
    # 높이 H, 너비 W

    battle_field = [list(input()) for _ in range(H)]
    # 게임 맵 battle_field
    # print(battle_field)

    N = int(input())
    # 사용자가 넣을 입력의 개수 N

    input_command = input()
    # 입력하는 길이가 N인 문자열 input_command

    '''
    전차 위치에서 델타응용으로?
    '''

    # 전차 위치 찾기
    tank_position = find_tank()

    # 전차 위치에서 입력값 종류에 따라 명령 실행
    # 포탄 쏠 때 전차가 바라보는 방향 고려해야함

    # 우 상 좌 하
    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    dd = ['>', '^', '<', 'v']
    dict_w = {'R': 0, 'U': 1, 'L': 2, 'D': 3}

    i, j = tank_position
    si, sj = tank_position  # 초기 위치 저장

    # 초기조건 탱크의 방향 저장
    direction_idx = dd.index(battle_field[i][j])    # [1]

    # input 들어오는 문자 확인해서 그에 따른 명령 실행
    for c in input_command:
        # Shoot 나오면 전에 설정한 방향대로 쏘기
        if c == 'S':
            # print(c)
            k = 1
            while True:
                # 초기 설정
                pi = i + di[direction_idx] * k
                pj = j + dj[direction_idx] * k

                # 포탄이 정상인덱스라면
                if 0 <= pi <= H - 1 and 0 <= pj <= W - 1:

                    # 벽돌벽이라면, 평지로 바꾼다.
                    if battle_field[pi][pj] == '*':
                        battle_field[pi][pj] = '.'
                        break

                    # 만약 강철벽이라면, 아무일도 일어나지 않음.
                    elif battle_field[pi][pj] == '#':
                        break

                else:       # 정상인덱스가 아니라면
                    break

                k += 1

        # 방향 명령이라면
        else:
            # print(c)
            # 방향 저장
            direction_idx = dict_w[c]
            # print(direction_idx)

            ni = i + di[dict_w[c]]
            nj = j + dj[dict_w[c]]

            if 0 <= ni <= H-1 and 0 <= nj <= W-1 and battle_field[ni][nj] == '.':   # 정상인덱스이고, 평지라면, 이동
                # 원래 자리 평지로 하고 이동.. 같은자리 다시 올 수 있도록
                battle_field[i][j] = '.'
                i = ni
                j = nj
                # print(i, j)
        # pprint.pprint(battle_field)
        # print()

    # 모든 입력 마치면 탱크의 초기위치와 현재 위치 수정
    # print(i, j)
    battle_field[si][sj] = '.'
    battle_field[i][j] = dd[direction_idx]

    # 배틀필드 출력
    print(f'#{test_case}', end=' ')
    for row in battle_field:
        print(''.join(row))




