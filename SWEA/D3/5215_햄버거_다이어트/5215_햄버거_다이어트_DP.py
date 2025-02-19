import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    point_and_kcal = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (L + 1)
    # dp[j] = 칼로리 j를 사용했을 때 얻을 수 있는 최대 점수

    for taste, cal in point_and_kcal:   # (100,200) (300, 500) (250, 300) (500, 1000) (400, 400)
        for j in range(L, cal - 1, -1):     # 제한 칼로리부터 현재 재료의 칼로리까지 역순으로
            dp[j] = max(dp[j], dp[j - cal] + taste)
            '''
            taste, cal = (100, 200)
            dp[1000]에 재할당한다.
                최댓값을 : 지금 dp[1000]와 dp[1000-200] + 100 중에서 
                처음엔 전부 0 이니까 j = 1000, 999, 998... 200 까지 전부 dp[j] = 100이 된다.
                
            taste, cal = (300, 500)
            dp[1000]에 재할당한다.
                최댓값을 : 지금 dp[1000](=100)와 dp[1000-300] + 500 중에서 
                    dp[1000] = dp[700] + 500
                             = 600
            
            dp[999]에 재할당한다.
                최댓값을 : 지금 dp[999](=100)와 dp[999-300] + 500 중에서
                    dp[999] = dp[699] + 500
                            = 600
                            .
                            .
                            .
            
                    
                
            
                

            '''


    print(f'#{t} {dp[L]}')
    # 1000kcal를 사용했을 때 얻을 수 있는 최대 점수

    '''
    kcal을 1kcal씩 나눠서 생각?
    문제에서 kcal가 100의 배수다, 10의 배수다 라는 말 없음.
        test case에서 장난치면 687kcal 이럴수도 있다.
        그래서 1kcal씩 나누는거
    '''

