import sys
sys.stdin = open('input.txt', 'r')

'''
지금 현재 기준으로, 
현재 시간대의 종료시간보다 시작시간이 큰 것 중에서, 
    종료시간 가장 작은 것 선택
이거 반복
'''


def greedy(idx):
    global max_v, cnt, L

    while idx < L:
        flag = 1
        for t in range(idx, L):
            if flag == 0:
                break
            # 가지치기
            # 현재 시간대 포함해서 남은 모든 시간대 합쳐도 max 못 넘을 때, 함수 종료
            if L - (t-1) < cnt:
                break
            for j in range(t+1, L):
                if lst_n[t][1] <= lst_n[j][0]:  # 시작시간이 현재 종료시간보다 높으면, 여기서 종료시간 가장 작은것 선택
                    idx = lst_n.index(min(lst_n[j::], key=lambda x: x[1]))
                    print(f'idx = {idx}')
                    cnt += 1
                    print(f'cnt = {cnt}')
                    flag = 0
                    break
        if flag == 1:
            break


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())

    # 신청서 인풋으로 받아서 받을때마다 정렬? 힙?
    # 그냥 다 받고 sort하자
    lst_n = []
    for i in range(N):
        lst_n.append(list(map(int, input().split())))

    lst_n.sort(key=lambda x: x[0])
    L = len(lst_n)
    max_v = 0
    cnt = 1

    greedy(0)

    print(f'#{test_case} {cnt}')
