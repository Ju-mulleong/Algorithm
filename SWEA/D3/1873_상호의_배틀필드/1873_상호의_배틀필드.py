import sys
sys.stdin = open('input.txt', 'r')


def find_tank():
    for i in range(H):
        for j in range(W):
            if battle_field[i][j] in '^><v':
                return i, j


T = int(input())    # 테스크 케이스의 개수 T

for test_case in range(1, 1+T):
    H, W = map(int, input().split())
    # 게임 맵은 H*W 크기의 격자판
    # 높이 H, 너비 W

    battle_field = [list(input()) for _ in range(H)]
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

    dw = ['R', 'U', 'L', 'D']

    i, j = tank_position
    for c in input_command:
        # 이동





