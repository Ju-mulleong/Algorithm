import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    point_and_kcal = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (L + 1)

    for taste, cal in point_and_kcal:   # (100,200) (300, 500) (250, 300) (500, 1000) (400, 400)
        for j in range(L, cal - 1, -1):     # 현재 제한 칼로리부터 현재 재료의 칼로리까지 역순으로
            dp[j] = max(dp[j], dp[j - cal] + taste)


    print(f'#{t} {dp[L]}')

    '''
    kcal을 1kcal씩 나눠서 생각?
    
    '''