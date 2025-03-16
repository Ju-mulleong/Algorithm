import sys
sys.stdin = open('input.txt' ,'r')


'''
target_1, target_2의 가장 가까운 공통조상 찾기
'''


def find_pp(n):
    global adj_lst, ans

    while n >= 1:   # 노드번호는 루트 이상
        if adj_lst[n][3] == 0:  # 미방문시
            adj_lst[n][3] = 1   # 방문 표시
            n = adj_lst[n][2]   # 부모로 n 바꾸기
        else:   # 방문했다면
            ans = n
            break

# 전위순회로 서브트리 크기 구하기
def pre_order(n):
    global adj_lst, cnt

    if n:
        cnt += 1
        pre_order(adj_lst[n][0])
        pre_order(adj_lst[n][1])


T = int(input())

for test_case in range(1, 1+T):
    V, E, target_1, target_2 = map(int, input().split())

    adj_lst = [[0]*4 for _ in range(V+1)]   # 왼쪽자식, 오른쪽자식, 부모, visited 순서

    temp_lst = list(map(int, input().split()))

    # 부모 자식 순서 간선 나열
    for i in range(E):
        p, c = temp_lst[i*2], temp_lst[i*2+1]

        if adj_lst[p][0] == 0:
            adj_lst[p][0] = c
        else:
            adj_lst[p][1] = c

        adj_lst[c][2] = p

    ans = 0

    # 공통조상 찾기

    find_pp(target_1)
    find_pp(target_2)

    cnt = 0
    # 공통조상 루트로 하는 서브트리 크기 찾기
    pre_order(ans)

    # 출력
    print(f'#{test_case} {ans} {cnt}')
