import sys
sys.stdin = open('input.txt', 'r')
import heapq

'''
족보 구하기
'''

def solve():
    global suit_lst, num_lst
    # 도형이 모두 같은가?(플러쉬, 로얄 플러쉬)
    for i in range(4):
        if suit_lst[i] != suit_lst[i + 1]:
            break


    for i in range(4):
        if num_lst[i] + 1 != num_lst[i+1]:
            break
    return ''



    # 스트레이트인가?






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
    print(suit_lst)
    print(num_lst)

    print(f'#{test_case} {solve()}')

