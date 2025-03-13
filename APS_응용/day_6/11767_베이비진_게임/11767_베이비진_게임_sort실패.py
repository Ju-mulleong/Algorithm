import sys
sys.stdin  = open('input.txt', 'r')


'''
현재 주어진 카드들로 run이나 tiplet을 만들수 있으면 만든다.
받은 카드들 오름차순으로 정렬하면 자연스럽게 확인 가능???

'''


def check(lst, winner):
    # 받은 카드들 오름차순으로 정렬
    lst.sort()
    # print(lst)
    for i in range(len(lst)-2):
        # run인가?
        if lst[i] + 1 == lst[i+1] and lst[i+1] + 1 == lst[i+2]:
            # print(winner)
            return winner

        # triplet인가?
        if lst[i] == lst[i+1] and lst[i+1] == lst[i+2]:
            # print(winner)
            return winner

    # 그냥 끝낸다면 무승부 0 반환
    return 0


T = int(input())

for test_case in range(1, 1+T):
    card_lst = list(map(int, input().strip().split()))

    lst_A = []
    lst_B = []
    win = 0

    for i in range(0, len(card_lst), 2):
        lst_A.append(card_lst[i])
        # lst_A의 크기가 3이상일 때
        if len(lst_A) >= 3:
            # run, 또는 triplet인지 확인하는 코드
            win = check(lst_A, 1)
            if win:
                break

        lst_B.append(card_lst[i+1])
        # lst_B의 크기가 3이상일 때
        if len(lst_B) >= 3:
            # run, 또는 triplet인지 확인하는 코드
            win = check(lst_B, 2)
            if win:
                break

    print(f'#{test_case} {win}')