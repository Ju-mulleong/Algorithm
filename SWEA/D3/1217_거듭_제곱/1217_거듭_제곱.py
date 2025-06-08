import sys
sys.stdin = open('input.txt', 'r')

T = 10


def solve(n, m, cnt):
    global result

    # 가지치기

    # 종료조건
    if m == cnt:
        return

    # 반복
    result *= n
    cnt += 1
    solve(n, m, cnt)


for test_case in range(1, 1+T):
    tc = int(input())

    # N의 M 거듭제곱 구하기, N, M
    N, M = map(int, input().split())

    result = N
    solve(N, M, 1)

    print(f'#{tc} {result}')