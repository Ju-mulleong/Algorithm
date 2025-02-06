# 입력값 받을 때 08271을 int로 받으면 8271 되버림, list로 받을 것

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # T는 테스트 케이스의 개수

for test_case in range(1, 1+T):

    N = int(input())    # N은 카드 장수
    num_list = []
    for i in input():   # num_list에 카드의 숫자들 저장
        num_list.append(int(i))

    print(N, num_list)

    # 0부터 9까지 숫자가 적힌 N장의 카드
    # 가장 많은 카드에 적힌 숫자와 총 카드가 몇 장인지 출력
    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽 출력

    # 카운팅 정렬의 '누적'까지 하고 그 원소들 비교하여 가장 큰 원소의 index가 most_num
    # 비교할 때 if문으로 카드 장 수가 같을 때 큰 쪽 할당

    # '누적' 작업 하기 위해 num_list의 최댓값 구하기
    max_num = 0
    for i in num_list:
        if i > max_num:
            max_num = i
    # print(max_num)

    # '누적'
    cnts = [0] * (max_num + 1)
    # print(cnts)
    for i in range(len(num_list)):    # num_list의 원소들 확인
        # num_list[i]가 4면 cnts[4]의 값 +1
        cnts[num_list[i]] += 1
    print(cnts)

    most_num_cnt = 0
    most_num = 0
    for i in range(len(cnts)):
        print(i,cnts[i], most_num)
        if cnts[i] > cnts[most_num]:
            # i가 가장 많은 카드의 숫자
            most_num = i
            most_num_cnt = cnts[i]  # 가장 많은 카드에 적힌 숫자의 장수

        elif cnts[i] == cnts[most_num]:
            if i > most_num:
                most_num = i
                most_num_cnt = cnts[i]  # 가장 많은 카드에 적힌 숫자의 장수

    print(f'#{test_case} {most_num} {most_num_cnt}')


