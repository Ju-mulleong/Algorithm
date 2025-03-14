import sys
sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output.txt', 'w')
'''
1일, 1달, 3달, 1년 
    전부 1일 기준으로 이 이용권으로 며칠동안 이용하면 1일 이용권보다 이득인지 체크?
3달 요금이 중요한듯
재귀? 3달요금을 0번, 1번, 2번... 최대 4번 사용할 때, 그때의 최적해
부분집합 느낌
'''


def apply_three_month(d, m, t, lst, n, cnt):
    global min_v
    print(f'cnt = {cnt}')
    print(f'lst = {lst}')
    if n == cnt:
        # 최솟값 업데이트
        min_v = min(min_v, day_month(d, m, t, lst, n))
        print(f'min_v = {min_v}')
        return

    for j in range(12):
        if lst[j]:
            print(f'j = {j}')
            temp_lst = [x for x in lst]
            print(f'temp_lst = {temp_lst}')

            if j == 10:
                lst[j], lst[j + 1] = 0, 0

            elif j == 11:
                lst[j] = 0

            else:
                lst[j], lst[j+1], lst[j+2] = 0, 0, 0

            apply_three_month(d, m, t, lst, n, cnt + 1)

            lst = temp_lst
            print(f'returned_lst = {lst}')


# 주어진 lst에서 하루요금, 한 달치 요금 조합의 최저가격 구하기
def day_month(d, m, t, lst, n):
    flag = m // d
    temp_sum = t*n
    for i in range(12):
        if lst[i]:
            if lst[i] > flag:  # 한 달 기준 한달요금이 하루요금보다 이득이면
                temp_sum += m
            else:  # 손해면
                temp_sum += lst[i]*d
    # print(f'temp_sum = {temp_sum}')
    return temp_sum


def greedy(d, m, t):
    global plan_lst, min_v

    min_price = 0xffffff

    # 3달 요금 0번, 1번, 2번, 3번, 4번 구매하기
    for n in range(5):
        # 3달 요금 적용한 달 0으로 바꿔서 return
        apply_three_month(d, m, t, plan_lst, n, 0)  # min_v 최솟값으로 업데이트

        min_price = min(min_price, min_v)

    return min_price


T = int(input())

for test_case in range(1, 1+T):
    # 가격 (1일, 1달, 3달, 1년)
    day, month, three_month, year = map(int, input().split())
    # print(day, month, three_month, year)

    # 이용계획
    plan_lst = list(map(int, input().split()))
    # print(plan_lst)

    # 1년짜리가 디폴트 비용
    min_v = year
    min_price = greedy(day, month, three_month)

    print(f'#{test_case} {min_price}')
    # print('-----------------------------------------')


'''
원복시 list통째로 복사하는거 하지말자.

재귀할때마다 temp_lst가 이전 시행의 temp_lst를 덮어씌운다.

'''