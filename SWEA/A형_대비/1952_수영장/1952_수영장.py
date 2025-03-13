import sys
sys.stdin = open('input.txt', 'r')

'''
1일, 1달, 3달, 1년 
    전부 1일 기준으로 이 이용권으로 며칠동안 이용하면 1일 이용권보다 이득인지 체크?
3달 요금이 중요한듯
재귀? 3달요금을 0번, 1번, 2번... 최대 4번 사용할 때, 그때의 최적해
부분집합 느낌
'''


def apply_three_month(d, m, t, lst, n, cnt):
    if n == cnt:
        # 남은 이용일수 m와 d로 채우기
        return day_month(d, m, lst)

    for j in range(12):
        if lst[j]:
            temp_lst = lst  # 원복용 temp_lst, 1차원리스트니까 그냥 할당해도된다.

            lst[j], lst[j+1], lst[j+2] = 0, 0, 0
            apply_three_month(d, m, t, lst, n, cnt+1)
            lst = temp_lst


# 주어진 lst에서 하루요금, 한 달치 요금 조합의 최저가격 구하기
def day_month(d, m, lst):
    # d = 0
    flag = m // d
    temp_sum = 0
    for i in range(12):
        if lst[i] > flag:  # 한 달 기준 한달요금이 하루요금보다 이득이면
            temp_sum += m
            lst[i] = 0
        else:  # 손해면
            temp_sum += d

    return temp_sum


def greedy(d, m, t):
    global plan_lst, min_v

    # 3달 요금 1번, 2번, 3번, 4번 사기
    for n in range(1, 5):
        # 3달 요금 적용한 달 0으로 바꿔서 return
        price = apply_three_month(d, m, t, plan_lst, n, 0)

        # 3달 요금 * i + day_month 리턴값
        # 기존 최솟값과 비교해서 업데이트
        min_v = min(min_v, t * n + price)


T = int(input())

for test_case in range(1, 1+T):
    # 가격 (1일, 1달, 3달, 1년)
    day, month, three_month, year = map(int, input().split())
    print(day, month, three_month, year)

    # 이용계획
    plan_lst = list(map(int, input().split()))
    print(plan_lst)
    print('-----------------------------------------')

    # 1년짜리가 디폴트 비용
    min_v = year
    greedy(day, month, three_month)

    print(f'#{test_case} {min_v}')