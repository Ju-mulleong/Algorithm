import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    binary_str = input()

    decimal_num = 0
    decimal_lst = []
    for i in range(1, len(binary_str)+1):
        j = -i

        c = i % 7
        if i % 7 == 0:
            c = 7
        decimal_num += int(binary_str[j]) * (2 ** (c-1))
        # print(decimal_num)

        if j % 7 == 0:     # 7bit마다 끊기
            decimal_lst.append(decimal_num)
            decimal_num = 0

    print(f'#{test_case} {" ".join(map(str, decimal_lst[::-1]))}')


