import sys
sys.stdin = open('input.txt', 'r')


'''
세 개 이상의 전선이 하나의 점에서 만나지 않는다
입력 다 받고 제일 작은 Ai부터 시작한다.
    자신보다 Ai가 높고, Bi가 낮은 경우, 교차점
    자신보다 Ai가 낮고, Bi가 높은 경우, 교차점
    그냥 전부 구해서 /2
'''


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    lst_all = [[0] for _ in range(N)]
    for i in range(N):
        [A, B] = list(map(int, input().split()))
        lst_all[i] = [A, B]
    # print(lst_all)

    cnt = 0
    for i in range(N):
        for j in range(N):
            if lst_all[i][0] < lst_all[j][0] and lst_all[i][1] > lst_all[j][1]:
                cnt += 1

            elif lst_all[i][0] > lst_all[j][0] and lst_all[i][1] < lst_all[j][1]:
                cnt += 1

    print(f'#{test_case} {cnt//2}')