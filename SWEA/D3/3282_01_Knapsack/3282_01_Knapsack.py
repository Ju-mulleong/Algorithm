import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

'''
1번부터 N번까지의 번호가 부여된 N개의 물건, 
K부피만큼 담을 수 있는 가방

1~N번 물건은 각각 부피 Vi, 가치 Ci 가진다.
가치의 합이 최대가 되도록 가방안에 물건 넣기

만약 물건을 부피1로 전부 쪼갤수 있으면 당연히 단위부피당 가치가 가장 큰 순서대로 넣으면 된다.
그런거 아니니까 DP로?

물건 최대 100개니까 dfs는 안된다.

무게가 큰 것부터 넣는데, 만약 무게가 같은것이있다면 단위부피당 가치가 큰 것부터?
메모이제이션?
'''


def dp():

    # i번째 물건까지 넣었을때, 남은 무게제한이 w인 arr[i][w]
    # 가로세로 0 더미
    arr = [[0]*(1+K) for _ in range(1+N)]

    for i in range(1, 1+N):
        for w in range(1+K):
            # 만약 현재 무게 제한보다 현재 물건 무게가 큰 경우, 어차피 배낭에 못넣음.
            # 그러므로 이전 까지 넣었던 물건들의 배낭 가치 유지
            # 남은 무게제한 또한 이전까지와 같음
            if weight_lst[i] > w:
                arr[i][w] = arr[i-1][w]

            # 만약 현재 무게제한보다 현재 물건 무게가 작은경우, 넣거나/넣지말거나 선택 가능
            # 둘 중 더 큰값을 기록
            else:
                arr[i][w] = max(arr[i-1][w], arr[i-1][w-weight_lst[i]] + value_lst[i])


    # 만약 최대 부피인 K를 달성못하는 조합이더라도,
    # 어차피 arr[N][K]는 모든 물건을 고려했을때, 무게가 K이하인 모든 조합 중 최대 가치를 의미한다.

    return arr[N][K]


for test_case in range(1, 1+T):
    # 물건의 개수 N, 가방의 부피 K
    N, K = map(int, input().split())

    # 부피, 가치 각각 리스트에 따로 저장.
    # 더미 0 넣어서 인덱스 맞추기
    weight_lst = [0]     # 부피
    value_lst = [0]     # 가치
    for i in range(N):
        w, v = map(int, input().split())
        weight_lst.append(w)
        value_lst.append(v)

    # print(value_lst, weight_lst)

    print(f'#{test_case} {dp()}')

