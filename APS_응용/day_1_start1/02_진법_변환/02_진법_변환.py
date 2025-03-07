target = 74

# 10진수를 2진수로 바꾸는 과정을 코드로 작성

# print(bin(74))
# print(hex(74))

def dec_to_binary(target):
    binary_number = ""

    while target > 0:
        remain = target % 2     # 2로 나눈 나머지
        binary_number = str(remain) + binary_number     # 새로 생긴 나머지 + 기존의 나머지 순서
        target = target // 2    # 2로 나눈다.
        # print(binary_number)
    print(binary_number)


def binary_to_decimal(binary_str):
    # 1. binary_str 문자열 뒤에서부터 진행
    # 2. 각 자리에 맞는 수를 곱하면서, 결과에 더한다.
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1

    print(decimal_number)


# 10진수 -> 16진수
def decimal_to_hexadecimal(target):
    hex_digit = "0123456789ABCDEF"
    # hex_digit[10] => A
    # hex_digit[15] => F
    hex_number = ""

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain] + hex_number
        target //= 16

    print(hex_number)

dec_to_binary(target)
binary_to_decimal("1001010")
decimal_to_hexadecimal(160)