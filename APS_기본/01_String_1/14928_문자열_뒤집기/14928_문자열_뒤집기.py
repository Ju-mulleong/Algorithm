import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for test_case in range(1, 1+T):
    len_str = int(input())  # 문자열의 길이 len_str
    lst_str = list(input())     # 목표 문자열 str_t를 리스트로 받기(가변시키기 위해)

    # 문자열의 길이의 절반만큼 ([i], [-1-i])... 를 서로 바꾼다.
    # 문자열이 짝수이면 전부 바꾸고 홀수이면 가운데 글자는 어차피 안 바뀌니 상관 없다.

    for i in range(len_str // 2):   # 문자열 길이 절반만 반복하면 됨
        if len_str <= 1:     # 한 글자 이하면 안 바꿔도 됨.
            break

        lst_str[i], lst_str[-1 - i] = lst_str[-1 - i], lst_str[i]
        # print(lst_str)

    print(f'#{test_case} {"".join(lst_str)}')




