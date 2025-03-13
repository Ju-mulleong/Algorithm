import sys
sys.stdin = open('input.txt', 'r')

'''
종료시간 기준으로 오름차순으로 정렬.
첫 인덱스 시작으로 range(i+1, L) 중에서
    앞에서부터 순서대로 순회, 시작시간이 현재 도착시간보다 큰 것 선택 cnt += 1
    반복
'''


def greedy(idx):
    global max_v, cnt, L

    ii = 0
    while ii < L:
        flag = 1
        for i in range(ii, L):
            if flag == 0:
                break
            # 가지치기
            # 현재 시간대 포함해서 남은 모든 시간대 합쳐도 max 못 넘을 때, 함수 종료
            if L - (i - 1) < cnt:
                break
            for j in range(i+1, L):
                if lst_n[j][0] >= lst_n[i][1]:
                    ii = j
                    cnt += 1
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

    lst_n.sort(key=lambda x: x[1])
    L = len(lst_n)
    max_v = 0
    cnt = 1

    greedy(0)

    print(f'#{test_case} {cnt}')
