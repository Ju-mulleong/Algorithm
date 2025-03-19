import sys
sys.stdin = open('input.txt', 'r')


'''
러시아 국기같은 깃발을 만들기 위해
새롭게 칠해야하는 칸의 최솟값 구하기
흰
파
빨
순서대로, 각 색깔은 최소 1줄 있어야 한다.
N행 M열의 깃발크기
3 <=  N and M <= 50

(흰, 파, 빨)의 합이 N이 되는 부분집합, 각 원소는 1보다 크다.
흰색과 파란색을 몇줄할지 정하면, 나머지 행은 자동으로 전부 빨간색 된다.

부분집합의 크기가 3, 
부분집합의 합이 N, 
부분집합의 각 원소는 1 <= 원소의 크기 <= N-2
그냥 dfs로 하나씩 더해서 cnt가 N이되면 해도 되긴함
N이 최대 50이니까 dfs보다 비트마스킹으로

'''


def color(w, b, r):
    # print(w, b, r)
    cnt = 0
    for i in range(1, N+1):

        if i <= w:
            cnt += M - arr[i-1].count('W')
        elif w < i <= w+b:
            cnt += M - arr[i-1].count('B')
        else:
            cnt += M - arr[i-1].count('R')

    return cnt


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 행, M은 열

    arr = [list((input())) for _ in range(N)]
    min_v = 0xffff

    for w in range(1, (N-2) + 1):
        for b in range(1, (N-2) + 1 - w + 1):
            # w, b 정하면 r는 정해진다.
            r = N - (w + b)

            cnt = color(w, b, r)
            min_v = min(min_v, cnt)

    print(f'#{test_case} {min_v}')


