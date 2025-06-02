import sys
sys.stdin = open('input.txt', 'r')


'''
매 초마다 커맨드 주어짐.
0은 유지, 
1, N 은 N의 가속도로 가속
2, M 은 M의 가속도로 감속
현재 속도보다 감속량이 큰 경우 속도는 0

가속/감속하는데 걸리는 시간은 0.(즉시 속도가 변경됨.)

N개의 커맨드를 N초동안 모두 수행했을 때, 이동한 거리 계산.
0초에서 커맨드 0
1초에서 커맨드 1...
'''


T = int(input())

for test_case in range(1, 1+T):
    # 커맨드의 수
    N = int(input())

    # 현재 시점까지 이동한 거리
    d = 0

    # 현재 시점에서 속도
    v = 0

    # 이번 테케에서 커맨드 받기
    for i in range(N):
        commands = list(map(int, input().split()))

        # commands가 현재속도 유지하면 속도 그대로

        # commands가 감속 또는 가속
        # 가속
        if commands[0] == 1:
            v += commands[1]

        # 감속
        elif commands[0] == 2:
            v -= commands[1]
            if v < 0:
                v = 0

        d += v

    print(f'#{test_case} {d}')
