import sys
sys.stdin = open('input.txt', 'r')

'''
1일, 1달, 3달, 1년 
    전부 1일 기준으로 이 이용권으로 며칠동안 이용하면 1일 이용권보다 이득인지 체크?
'''

T = int(input())

for test_case in range(1, 1+T):
    # 가격 (1일, 1달, 3달, 1년)
    day, month, three_month, year = map(int, input().split())

    # 이용가격
    plan_lst = list(map(int, input().split()))
    print(plan_lst)
