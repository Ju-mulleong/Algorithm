import sys
sys.stdin = open('input.txt', 'r')


n_dic = {'A': 0, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}
s_dic = {'S': 0, 'D': 1, 'H': 2, 'C': 3}

T = int(input())

for tc in range(1, T + 1):
    card = input().split()
    n = [0] * 13
    s = [0] * 4
    for i in range(5):
        s[s_dic[card[i][0]]] += 1
        if card[i][1] in n_dic:
            n[n_dic[card[i][1]]] += 1
        else:
            n[int(card[i][1]) - 1] += 1

    f = 1
    if f and max(s) == 5:
        score = 0
        new_n = n + [n[0]]
        for i in range(13):
            if new_n[i] == 1 and new_n[i + 1] == 1:
                score += 1
                if score == 4:
                    print(f'#{tc} Straight Flush')
                    f = 0
                    break
            else:
                score = 0

    if f and max(n) == 4:
        print(f'#{tc} Four of a Kind')
        continue

    if f and max(n) == 3 and n.count(2) == 1:
        print(f'#{tc} Full House')
        continue

    if f and max(s) == 5:
        print(f'#{tc} Flush')
        continue

    if f and max(n) == 1:
        score = 0
        new_n = n + [n[0]]
        for i in range(13):
            if new_n[i] == 1 and new_n[i + 1] == 1:
                score += 1
                if score == 4:
                    print(f'#{tc} Straight')
                    f = 0
                    break
            else:
                score = 0

    if f and max(n) == 3:
        print(f'#{tc} Three of a kind')
        continue

    if f and max(n) == 2:
        if n.count(2) == 2:
            print(f'#{tc} Two pair')
            continue
        else:
            print(f'#{tc} One pair')
            continue

    if f:
        print(f'#{tc} High card')