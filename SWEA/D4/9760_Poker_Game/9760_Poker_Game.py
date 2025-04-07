import sys
sys.stdin = open('input.txt', 'r')

'''
족보 구하기
'''


def is_straight():
    global num_lst
    # 스트레이트인가?
    # 로얄 스트레이트인가?
    if num_lst == [1, 10, 11, 12, 13]:
        return True

    for i in range(4):
        if num_lst[i]+1 != num_lst[i+1]:
            break
    else:
        return True


def solve():
    global suit_lst, num_lst
    # 스트레이트 먼저 파악하기
    flag = is_straight()

    # 도형이 모두 같은가?(플러쉬, 스트레이트 플러쉬)
    for i in range(4):
        if suit_lst[i] != suit_lst[i + 1]:
            break

    else:
        if flag:
            return 'Straight Flush'

        else:
            # 플러쉬
            return 'Flush'

    if flag:
        return 'Straight'

    # 값으로 결정되는 족보들(포카드, 풀 하우스, 트리플, 투 페어, 원 페어, 하이카드)
    # 카운트 정렬
    count_lst = [0]*14
    for i in range(5):
        count_lst[num_lst[i]] += 1
    # print(count_lst)
    # print(start, end)

    # 카운트 정렬한 리스트에서 0 제거
    count_lst = [x for x in count_lst if x != 0]
    count_lst.sort(reverse=True)
    # print(count_lst)

    if count_lst == [4, 1]:
        return 'Four of a Kind'
    elif count_lst == [3, 2]:
        return 'Full House'
    elif count_lst == [3, 1, 1]:
        return 'Three of a kind'
    elif count_lst == [2, 2, 1]:
        return 'Two pair'
    elif count_lst == [2, 1, 1, 1]:
        return 'One pair'
    else:
        return 'High card'

    # # count_lst의 길이로 족보 파악 가능
    # l = len(count_lst)
    # if l == 2:     # 포카드 또는 풀하우스
    #     if 4 in count_lst:
    #         return 'Four of a Kind'
    #     else:
    #         return 'Full House'
    # elif l == 3:
    #     if 3 in count_lst:
    #         return 'Three of a kind'
    #     else:
    #         return 'Two pair'
    # elif l == 4:
    #     return 'One pair'
    # elif l == 5:
    #     return 'High card'


T = int(input())

for test_case in range(1, 1+T):
    # [(S, 1), (S, 2), (D, 1), (H, 1), (C, 1)] 형태로 저장하기
    suit_lst = []
    num_lst = []
    to_num = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}

    for card in input().split():
        suit_lst.append(card[0])

        if card[1] in to_num.keys():
            num_lst.append(to_num[card[1]])
            continue
        else:
            num_lst.append(int(card[1]))

    num_lst.sort()
    suit_lst.sort()
    # print(num_lst)
    # print(suit_lst)
    print(f'#{test_case} {solve()}')

