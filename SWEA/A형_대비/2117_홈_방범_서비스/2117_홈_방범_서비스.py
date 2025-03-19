import sys
sys.stdin = open('input.txt', 'r')


'''
놀랍게도 이 보안회사는 회사의 이익보다 방법서비스를 받는 고객의 수를 우선시한다.
손해를 보지 않는 한 가장 많은 집에 서비스를 제공하는 경우를 찾고, 그 집들의 수 출력

DFS or BFS

K는 무한정으로 커질수있다.
가장 먼저 생각나는 방법은 k = n에서의 범위를 인덱스마다 구할 수 있으니까, 
그냥 for i for j로 하나씩 범위 다 구해서 때려넣기 근데 이건 너무 낭비인듯

운영 비용은 서비스 영역의 면적과 동일하다.
테스트케이스별로 각 운영 영역마다 손익분기점인 집 수를 알 수 있다.
예를 들어 M = 2이면, 
집마다 내는 비용이 주어지니까, 
이 인덱스에서 어떤 크기에서 멈춰야하는지 알 수 있나?

주어진 arr에서 집 세기

빈칸에서 시작했을때도 최대 집이 될 수 있지 않나?
모르겠다 일단 다 넣어보자
'''


def solve(i, j, K):
    if K == 0:
        return

    global max_v
    # 현재 인덱스에서 시작
    # 구한 최대 K에서 시작, 손익분기점 넣는지 확인한다.
    # 안되면 K하나씩 줄이면서 확인해본다.
    # 되는 K에서 최댓값 비교

    # 현재 K와 인덱스로 운영 영역 확인하기

    # 가운데줄에서 확인
    kk = -1
    cnt = 0
    dd = 1
    for jj in range(j - (K-1), j + (K-1)+1):            # j-(K-1) ~ j+(K+1)
        kk += dd

        if kk == K - 1:
            dd = -1

        # 정상인덱스라면, ii 확인
        if jj < 0 or jj >= N:   # 비정상인덱스면 넘기기
            continue
        # print(f'kk = {kk}')

        for ii in range(i-kk, i+kk+1):
            # 이 인덱스가 정상인덱스라면, 집 있는지 확인
            if ii < 0 or ii >= N:  # 비정상인덱스일때 넘기기
                continue

            # print(f'i = {i}, j = {j}')
            # print(f'ii = {ii}, jj = {jj}, K = {K}')
            if arr[ii][jj] == 1:
                cnt += 1

    # 현재 영역안의 집들로 현재 선택한 영역의 손익분기점 넘을 수 있을 때 최댓값 업데이트 시도
    if cnt * M >= K * K + (K - 1) * (K - 1):
        max_v = max(max_v, cnt)
        return

    # 못넘으면, K 줄여서 다시 반복
    else:
        solve(i, j, K-1)


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N*N 크기의 도시, M은 하나의 집이 지불하는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 현재 테케의 맵에서 집의 총 개수 확인
    sum_house = 0
    for i in range(N):
        sum_house += arr[i].count(1)
    # print(sum_house)

    # 이번 테케에서 주어진 집 개수를 바탕으로 이론상 가능한 최대 영역을 알 수 있다.
    K = 1
    while M * sum_house > K * K + (K - 1) * (K - 1):   # 모든 맵에 있는 집을 다 포함해도 손익분기점 못넘길때까지 K더하기
        K += 1

    K = K - 1
    # print(K)

    max_v = 0
    for i in range(N):
        for j in range(N):
            solve(i, j, K)

    print(f'#{test_case} {max_v}')

'''
크기 비교할때 경계값 주의..
손익분기점이랑 같을때도 당연히 가능하다.(손익분기점 넘거나 같을때)
'''


