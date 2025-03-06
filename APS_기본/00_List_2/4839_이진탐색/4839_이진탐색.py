import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

# 이진탐색으로 A, B중 더 빨리 목표쪽수를 찾는 사람이 승자.
# 승자 출력, 비긴 경우는 0 출력


def find_book_number(P, Pa):
    start = 1
    end = P
    cnt = 0

    while start < end:
        middle = (start + end) // 2     # middle 초기화
        cnt += 1    # 매 실행마다 cnt 증가

        if middle == Pa:

            # print(cnt)
            return cnt

        elif middle > Pa:     # 목표값이 middle보다 왼쪽 영역에 있다면
            end = middle

        elif middle < Pa:
            start = middle   # 목표값이 middle보다 오른쪽 영역에 있다면

    return cnt


for test_case in range(1, 1+T):
    P, Pa, Pb = map(int, input().split())
    # P는 전체 쪽수
    # Pa, Pb는 각각 A, B가 찾아야 할 쪽수

    A_cnt = find_book_number(P, Pa)
    B_cnt = find_book_number(P, Pb)
    winner = ''

    if A_cnt > B_cnt:
        winner = 'B'
    elif A_cnt < B_cnt:
        winner = 'A'
    else:
        winner = "0"

    print(f'#{test_case} {winner}')

'''
처음에는 end = middle - 1, start = middle + 1 이였는데 tc 10개 중 2개 틀림
이렇게 해버리면, end = middle, start = middle 로 할 때보다 
더 빠르게 찾거나, 더 느리게 찾는다.
온라인 강의로 배운건 -1 하는 방법이지만, 
이 문제에서는 '누가 이겼는지'를 구하는 것이기에 정해진 방법으로 횟수를 구해야 한다.
-1로 하면 문제에서 상정한 답과 달라질 수 있음.
문제에서 end = middle, start = middle로 하라고 했으니까 그렇게 해야함.
'''
