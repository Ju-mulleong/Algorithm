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
    print(battle_field)
    '''
    전차 위치에서 델타응용으로?
    '''

    # 전차 위치 찾기
    tank_position = find_tank()

    # 전차 위치에서 처음에 주어진 '^><v' 종류에 따라 명령 실행
    while



