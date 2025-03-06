import sys
import pprint
sys.stdin = open('input.txt', 'r')


'''
언제나 암호는 1로 끝난다.
주어진 암호코드는 주어진 규칙대로 해독할 수 있음을 보장한다
행 방향 우선순회로 '끝에서부터' 검사한다.
    1 나오면, 그 자리에서 다시 검사방향으로 7자리 세고, 그 숫자 해독해서
        슬라이싱?
        슬라이싱보다 바로 계산해서 계속 합산하는게 나을듯
    이걸 8번 반복하고, 문자열 뒤집어서
        올바른지 아닌지 확인
'''

dict_b = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3' , '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'
}


def sol():
    for i in range(N):
        for j in range(-1, -M - 1, -1):
            if arr[i][j] == '1':  # 1 발견하면, 이 자리에서부터 7자리 세기
                decimal_str = ''
                cnt = 0
                while cnt < 8:
                    # print(cnt)
                    binary_str = ''
                    for k in range(7):  # k = 0, 1, 2, 3..., 6
                        binary_str = arr[i][j - k] + binary_str
                        # print(binary_str)

                    # 7자리 다 검사했으면, dict_b 의 키에 해당하는 값으로 변환
                    decimal_str = dict_b[binary_str] + decimal_str
                    j -= 7
                    cnt += 1

                return decimal_str


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # 배열은 M*N크기 N이 세로다!

    arr = [list(input()) for _ in range(N)]
    # for i in range(N):
    #     print(arr[i])

    password = sol()
    # print(password)

    sum_odd = 0
    sum_even = 0
    sum_password = 0
    for i in range(8):
        if i % 2 == 0:      # 0번 인덱스가 홀수, 시작
            sum_odd += int(password[i])

        else:
            sum_even += int(password[i])

        sum_password += int(password[i])

    if (sum_odd*3 + sum_even) % 10 == 0:
        ans = sum_password
    else:
        ans = 0

    print(f'#{test_case} {ans}')






