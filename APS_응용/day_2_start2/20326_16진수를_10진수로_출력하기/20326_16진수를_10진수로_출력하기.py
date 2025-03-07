import sys
sys.stdin = open('input.txt', 'r')


'''
16진수문자로 이루어진 1차배열이 주어진다.
2진수로 바꾼 후, 7bit씩 끊어서 십진수로 변환하여 출력
'''


def bin_to_dec(n):
    sum_v = 0
    for i in range(n):
        sum_v += int(binary_temp_str[-i - 1]) * 2 ** i
    # print(sum_v)
    return str(sum_v)


hex_dict = {'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

T = int(input())

for test_case in range(1, 1+T):
    hex_str = input()
    # print(hex_str)

    # 인풋값 2진수로 바꾸기
    binary_str =''
    for i in hex_str:
        if i in hex_dict:   # 문자면 딕셔너리에서 값 바로 넣기
            binary_str = binary_str + hex_dict[i]
        # 정수면 이진수로 변환
        else:
            i = int(i)
            temp = ''

            for j in range(-1, -5, -1):
                temp = str(i % 2) + temp
                i //= 2

            binary_str = binary_str + temp
    # print(binary_str)

    ans_lst = []
    for b in range(0, len(binary_str)+1, 7):
        # binary_str[0:7]
        # binary_str[7:14]
        # binary_str[14:21] ...

        # 슬라이싱 ~까지에 해당하는 숫자가 binary_str 전체길이 +1 보다 큰 경우
        # binary_str[그때의 시작값::]

        # 7bit짜리 받아서 십진수로 변환
        if b + 7 > len(binary_str)+1:
            binary_temp_str = binary_str[b:]
            ans_lst.append(bin_to_dec(len(binary_str) - b))
        else:
            binary_temp_str = binary_str[b:b+7]
            ans_lst.append(bin_to_dec(7))

    print(f'#{test_case} {" ".join(ans_lst)}')













