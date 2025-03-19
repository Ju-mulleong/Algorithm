import sys
sys.stdin = open('input.txt', 'r')


def find_root(n):
    while p_lst[n] != n:
        n = p_lst[n]
    return n


def union(a, b):
    # 문제에서 뭐가 대표자인지는 안 줌, 임의로 하면 될 듯?
    p_lst[find_root(a)] = p_lst[find_root(b)]


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 사람 수, M은 그룹 신청서 개수
    # 즉, M번 union 실행한다.

    # 신청서 쌍을 input으로 준다.
    application_lst = list(map(int, input().split()))

    # make_set
    lst = list(range(N+1))
    p_lst = [x for x in lst]

    # union 실행
    for i in range(M):
        union(application_lst[i*2], application_lst[i*2+1])
        # print(lst)
        # print(p_lst)
        # print()

    set_lst = set()
    for k in range(1, N+1):
        set_lst.add(find_root(k))
        # print(set_lst)

    print(f'#{test_case} {len(set_lst)}')