import sys
sys.stdin = open('input.txt', 'r')


'''
최대가 되는 경우를 내가 찾는게 나은가?
아니면 모든 경우를 순회하는게 나은가?

연산자 순열만들어서 트리?
트리는 하지말자 모양 이상함

연산자 순열 만들고, 
    그대로 계산
    계산 후 최댓값, 최솟값 업데이트

최댓값 - 최솟값 출력
'''


# 연산자 순열 만들기
# 더미 0 + 순열 형태
def permute(cal_per, cnt):
    # cal_per = '0'으로 시작
    dd = ['+', '-', '*', '/']

    # 연산자 다 정렬하면, 계산
    if cnt == (N-1):
        # print(cal_per)
        cal(cal_per)
        return

    # 순열 만들기
    for i in range(4):
        if cal_lst[i]:
            cal_lst[i] -= 1

            permute(cal_per + dd[i], cnt+1)

            cal_lst[i] += 1


# 계산하기
def cal(cal_per):
    global max_v, min_v, ccnt

    result = num_lst[0]
    for i in range(1, N):
        if cal_per[i] == '+':
            result = result + num_lst[i]

        elif cal_per[i] == '-':
            result = result - num_lst[i]

        elif cal_per[i] == '*':
            result = result * num_lst[i]

        elif cal_per[i] == '/':
            if result < 0:
                result = -((-result) // num_lst[i])
            else:
                result = result // num_lst[i]


    # 최종결과로 최댓값, 최솟값 업데이트
    if ccnt == 0:
        max_v = result
        min_v = result

    else:
        if result > max_v:
            max_v = result
        elif result < min_v:
            min_v = result
    ccnt += 1

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # N은 적혀있는 숫자의 개수

    cal_lst = list(map(int, input().split()))
    # +, -, *, / 순서대로 저장

    num_lst = list(map(int, input().split()))
    # 숫자 리스트에 저장 , 숫자 순서 고정!!

    ccnt = 0
    permute('0', 0)
    # print(max_v, min_v)

    print(f'#{test_case} {max_v - min_v}')



