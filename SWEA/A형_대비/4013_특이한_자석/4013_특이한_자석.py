import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


'''
주어진 순서 그대로 날의 정보를 받는다고 치면, 
    점수 확인하는 날의 인덱스는 0, 회전 확인하는 날의 인덱스는 2 또는 6이다.
    deque의 rotate?

1번 자석의 2번 인덱스 - 2번 자석의 6번 인덱스
2번 자석의 2번 인덱스 - 3번 자석의 6번 인덱스
3번 자석의 2번 인덱스 - 4번 자석의 6번 인덱스
'''


def check(checked, check_rotate, cur_num, cur_r, direction):
    # direction 에 따라 함수 한번만 호출하고 체크 여러번 수행할 수 있도록

    if 'R' in direction:
        # 현재 자석 기준 오른쪽 자석 확인
        if magnets[cur_num][2] + magnets[cur_num + 1][6] == 1:
            # 체크 안했으면, 체크 실행
            if checked[cur_num + 1] == 0:
                check_rotate.append((cur_num + 1, -cur_r))
                checked[cur_num + 1] = -cur_r

    if 'L' in direction:
        # 현재 자석 기준 왼쪽 자석 확인
        if magnets[cur_num][6] + magnets[cur_num - 1][2] == 1:
            # 체크 안했으면, 체크 실행
            if checked[cur_num - 1] == 0:
                check_rotate.append((cur_num - 1, -cur_r))
                checked[cur_num - 1] = -cur_r


def solve(m_num, m_r):
    global magnets

    # deque의 메서드 .rotate(n) 사용, n만큼 q를 회전시키는 것처럼 q의 원소들 인덱스 변경
    check_rotate = deque([(m_num, m_r)])  # 연동되어서 회전하는 자석 있는지 확인 위한 리스트
    checked = [0] * 5  # 회전 확정된 자석 리스트 (더미 0 포함)
    checked[m_num] = m_r

    # 현재 회전시켜야되는 자석과 맞닿아있는 자석날 확인
    while check_rotate:
        # dequeue
        cur_num, cur_r = check_rotate.popleft()

        # 자석이 2번, 3번이면 오른쪽 왼쪽 둘 다 봐야됨.
        if cur_num in (2, 3):
            # 왼쪽, 오른쪽 확인
            check(checked, check_rotate, cur_num, cur_r, 'LR')

        # 1번 자석이라면, 오른쪽만 확인
        elif cur_num == 1:
            # 현재 자석 기준 오른쪽 자석 확인
            check(checked, check_rotate, cur_num, cur_r, 'R')

        # 4번 자석이라면, 왼쪽만 확인
        else:
            # 현재 자석 기준 왼쪽 자석 확인
            check(checked, check_rotate, cur_num, cur_r, 'L')

        print(f'checked = {checked}')

    # 회전시키기
    for i in range(1, 5):
        if checked[i] == 1:
            magnets[i].rotate(1)
            print(f'{i}번 자석을 시계방향으로 회전!')
            print(magnets)
        elif checked[i] == -1:
            magnets[i].rotate(-1)
            print(f'{i}번 자석을 반시계로 회전!')
            print(magnets)


T = int(input())

for test_case in range(1, 1 + T):
    # 자석을 회전시키는 횟수 K
    K = int(input())

    # 4개의 자석 날의 정보, 날의 총 개수 = 8 ,index = (0~7)
    # 1 = N극, 0 = S극
    magnet_1 = deque(list(map(int, input().split())))
    magnet_2 = deque(list(map(int, input().split())))
    magnet_3 = deque(list(map(int, input().split())))
    magnet_4 = deque(list(map(int, input().split())))

    magnets = [[0], magnet_1, magnet_2, magnet_3, magnet_4]
    print(magnets)

    # (회전시키는 자석의 번호, 회전방향)의 쌍이 K번 주어진다.
    # 1칸 회전!!!
    for m in range(K):
        m_num, m_rotate = map(int, input().split())
        solve(m_num, m_rotate)

    # 점수 확인
    score = [1, 2, 4, 8]
    # print(magnets)
    ans = magnet_1[0] * score[0] + magnet_2[0] * score[1] + magnet_3[0] * score[2] + magnet_4[0] * score[3]

    print(f'#{test_case} {ans}')
    print()
