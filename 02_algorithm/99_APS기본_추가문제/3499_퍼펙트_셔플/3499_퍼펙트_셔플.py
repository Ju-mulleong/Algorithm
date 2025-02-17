import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    # 퍼펙트 셔플: 반갈라가지고 교대로 넣기

    # 슬라이싱?
    # 절반으로 슬라이싱해서 리스트 2개 만든 다음에
    # 아예 새로운 리스트에 하나씩 넣기
    N = int(input())

    lst = list(input().split())
    new_lst = []

    if N % 2 == 0:  # N이 짝수면
        lst_first = lst[:(N//2):]     # lst 앞에서부터 절반 슬라이싱
        lst_second = lst[(N//2)::]    # 절반 시작부터 끝까지 슬라이싱

    else:   # N이 홀수이면
        lst_first = lst[:(N // 2) + 1:]  # lst 앞에서부터 절반 슬라이싱
        lst_second = lst[(N // 2) + 1::]  # 절반 시작부터 끝까지 슬라이싱

    for i in range(len(lst)):
        if i%2 == 0:
            new_lst.append(lst_first.pop(0))
        else:
            new_lst.append(lst_second.pop(0))

    print(f'#{test_case} {" ".join(new_lst)}')



