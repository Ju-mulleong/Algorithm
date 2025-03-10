import sys
sys.stdin = open('input.txt', 'r')

'''
일단 16진수 로 이루어진 배열 받는다.
암호코드는 무조건 1로 끝난다.
    
'''


def is_right_password(hex_str):
    # 받은 16진수 2진수로 변환
    # 16진수를 10진수로 바꾼 다음에 10진수를 2진수로 바꾼다(4자리 맞추기)
    bin_str = format(int(hex_str, 16), '04b')
    print(bin_str)

    pass


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 세로크기, M은 가로크기

    i = 0
    while i < N-1:
        for j in input().strip():
            print(j)
            hex_str = ''
            if j != '0':
                hex_str = hex_str + j

            # 암호 확인
            is_right_password(hex_str)
        i += 1

