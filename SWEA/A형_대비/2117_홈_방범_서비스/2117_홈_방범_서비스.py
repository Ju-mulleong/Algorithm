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

def solve(i, j):
    # 현재 인덱스에서 시작
    # 구한 최대 K에서 시작, 손익분기점 넣는지 확인한다.
    # 안되면 다음 i, j로 넘어간다.
    # 모든 i, j 돌았는데도 안되면, K하나 내리고 다시 반복

    # 현재 K와 인덱스로 운영 영역 확인하기
    # 가운데줄 더하고
    # 가운데 기준 위와 아래 계산, j의 부호만 뒤집어주면 되니까 동시에 가능할듯





    pass





T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N*N 크기의 도시, M은 하나의 집이 지불하는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum_house = 0
    for i in range(N):
        sum_house += arr[i].count(1)
    # print(sum_house)

    # 이번 테케에서 주어진 집 개수를 바탕으로 이론상 가능한 최대 영역을 알 수 있다.
    K = 1
    # cost_K = K * K + (K - 1) * (K - 1)

    while M * sum_house > K * K + (K - 1) * (K - 1):   # 모든 맵에 있는 집을 다 포함해도 손익분기점 못넘길때까지 K더하기
        K += 1

    print(K)





    for i in range(N):
        for j in range(N):
            solve(i, j)





