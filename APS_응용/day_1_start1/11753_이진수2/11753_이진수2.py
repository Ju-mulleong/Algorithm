import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def get_binary_str(float_decimal):
    binary_str = ''
    i = 1
    while float_decimal:
        n = 2**(-i)
        if float_decimal >= n:
            float_decimal -= n
            binary_str += '1'
        else:
            binary_str += '0'

        if len(binary_str) > 12:
            return 'overflow'
        i += 1

    return binary_str


for test_case in range(1, 1+T):
    float_decimal = float(input())
    # print(float_decimal)

    '''
    나머지 계속 구해서 빈 문자열에 더해서 넣기 
    만약 문자열 길이 13 이상이면 'overflow' 출력
    '''

    print(f'#{test_case} {get_binary_str(float_decimal)}')