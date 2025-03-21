import sys
sys.stdin = open('input.txt', 'r')


'''
현재 인덱스 트럭으로 옮길수 있는 가장 큰 짐 옮기기
'''

T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 컨테이너 수, M은 트럭 수

    w_lst = list(map(int, input().split()))
    # 화물의 무게 w_lst

    t_lst = list(map(int, input().split()))
    # 트럭의 적재용량 t_lst

    # 컨테이너들 무게 기준 내림차순으로 정렬
    w_lst.sort(reverse=True)
    # print(w_lst)

    # 트럭 적재용량 기준 내림차순으로 정렬
    t_lst.sort(reverse=True)
    # print(t_lst)

    sum_v = 0
    # 제일 적재용량 큰 트럭이 컨테이너들중에서 적재용량 이하 중 가장 무거운 컨테이너 옮기기
    for t in range(len(t_lst)):
        w = 0
        # print(w_lst)
        while w < len(w_lst):
            if w_lst[w] <= t_lst[t]:
                sum_v += w_lst[w]
                pp = w_lst.pop(w)
                # print(pp)
                break
            w += 1
    print(f'#{test_case} {sum_v}')