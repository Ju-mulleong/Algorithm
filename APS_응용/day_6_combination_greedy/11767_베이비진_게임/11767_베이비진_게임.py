import sys
sys.stdin  = open('input.txt', 'r')


'''
현재 주어진 카드들로 run이나 tiplet을 만들수 있으면 만든다.
#### 받은 카드들 오름차순으로 정렬하면 자연스럽게 확인 가능
        !!! 아님.
만약 오름차순으로 정렬해서 받는다면 
001122를 받을 떄, 기존코드에서 run을 판별불가.

'''


def check(lst, winner):
    # print(lst)
    count_lst = [0] * 10  # 0 ~ 9

    # triplet?
    for i in range(len(lst)):
        count_lst[lst[i]] += 1
        if count_lst[lst[i]] == 3:
            return winner
    # print(count_lst)

    # run?
    for j in range(len(count_lst)-2):
        if count_lst[j] >= 1 and count_lst[j+1] >= 1 and count_lst[j+2] >= 1:
            return winner

    return 0

T = int(input())

for test_case in range(1, 1+T):
    card_lst = list(map(int, input().split()))

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