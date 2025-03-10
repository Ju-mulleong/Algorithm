import sys
sys.stdin = open('input.txt', 'r')


'''
구매는 하루에 최대 1만큼 가능하다.
판매는 얼마든지, 언제든지 할 수 있다.
'''


def solve(lst):
    global profit
    # 받은 lst의 길이가 1이하이면 종료(0이면 살 수 없고, 1이면 사는게 손해다.)
    if len(lst) <= 1:
        return

    max_v = 0
    max_idx = 0
    for i in range(len(lst)):
        if lst[i] >= max_v:     # 크거나 같을 때
            max_v = lst[i]
            max_idx = i

    # 최댓값 앞까지의 인덱스들(슬라이싱)을 최댓값에서 빼서 합산(이익)
    new_lst = lst[:max_idx]
    # print(new_lst)
    for j in new_lst:
        profit += max_v - j
        # print(profit)

    # 최댓값 다음 인덱스부터 슬라이싱한 리스트로 다시 재귀
    solve(lst[max_idx+1:])


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 원재는 연속된 N일 동안의 물건의 매매가를 알고 있다.

    price_lst = list(map(int, input().split()))
    profit = 0
    solve(price_lst)

    print(f'#{test_case} {profit}')