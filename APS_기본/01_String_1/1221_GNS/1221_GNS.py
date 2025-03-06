import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for test_case in range(1, 1 + T):

    tc, len_tc = input().split()   # tc는 #n 모양의 테스트 케이스 번호, len_tc는 단어의 개수

    arr = list(input().split())
    # print(arr)
    # 딕셔너리 써도 되나?

    # 빈 리스트 생성
    # counting_list = [0]*10

    # 탐색정렬이었나 그거 할 때처럼
    # ZRO면 counting_list[0]을 += 1 한다.
    # 그걸 for로 돌려서 전부 하고
    # counting_list의 각각 인덱스의 값만큼 해당하는 문자열 반복
    # 근데 이렇게 하면 for문 너무 길어지는데 if를 10개 써야하니까
    # 그러면 방법을 조금 바꿔보자

    word_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # word_list의 인덱스의 값과 글자가 같으면 새로운 리스트 만들어서 인덱스에 +1

    cnt_list = [0] * 10

    for i in range(len(arr)):
        for j in range(len(word_list)):
            if arr[i] == word_list[j]:
                cnt_list[j] += 1

    # print(cnt_list)

    # print(cnt_list)
    # 이 문제는 같은 단어들간의 차이 없다. 하트1, 스페이드1 같은게 아님. ZRO는 전부 ZRO
    # 그래서 뒤에서 부터 할 필요없음
    # 그냥 for로 값 꺼내고 그만큼 print 곱하면 될듯

    # 이거 설마 하나의 문자열로 출력해야하나
    #   그냥 word_list 잘못 써서 틀린거였음
    # 그러면 순서대로 이루어진 리스트 만들고, 그걸 join으로 공백으로 이으면 될 듯

    # ans_list = []
    #
    # for i in range(len(cnt_list)):
    #     # print(cnt_list[i])
    #     if cnt_list[i] == 0:
    #         continue
    #     for _ in range(cnt_list[i]):
    #         ans_list.append(word_list[i])
    #
    # print(tc)
    # # print(ans_list)
    # print(' '.join(ans_list))

    # for로 리스트 만들고 join해서 출력하는 것보다
    # print를 이어붙이는게 더 실행시간 빠르다

    print(tc)
    for i in range(len(cnt_list)):
        # print(cnt_list[i])
        if cnt_list[i] == 0:
            continue
        print(f'{word_list[i]} ' * cnt_list[i], end='')
    print(f'\n', end='')


'''
문제에서 요구하는 출력형식
문자열 2줄로 작성할 때 주의
'''








