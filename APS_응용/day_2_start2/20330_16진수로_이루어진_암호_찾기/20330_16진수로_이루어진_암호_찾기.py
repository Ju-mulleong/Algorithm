import sys
sys.stdin = open('input.txt', 'r')

dict_password = {'001101': '0', '010011': '1', '111011': '2', '110001': '3',
                 '100011': '4', '110111': '5', '001011': '6', '111101': '7',
                 '011001': '8', '101111': '9', }


def solve():
    global ans_str
    # 뒤에서부터 읽어서 1 만나면 확인 시작(모든 패턴은 1로 끝남)
    i = -1
    while i > -len(bin_str):
        # print(i)
        if bin_str[i] == '1':
            # 1포함 자리부터 6자리 확인
            temp_str = ''
            for j in range(6):  # 0, 1, 2, 3, 4, 5
                # 만약 i-j가 -len(bin_str)보다 작아진다면, 종료
                if i - j < -len(bin_str):
                    return

                temp_str = bin_str[i - j] + temp_str
            if temp_str in dict_password.keys():
                ans_str = dict_password[temp_str] + ' ' + ans_str
                i -= 6
                continue
        else:
            i -= 1

T = int(input())

for test_case in range(1, 1+T):
    str_password = input()
    bin_str = ''
    ans_str = ''

    for i in str_password:
        key_word = format(int(i, 16), 'b')
        # print(f'keyword: {key_word}')

        if len(key_word) < 4:
            while len(key_word) < 4:
                key_word = '0' + key_word
            # print(f'keyword: {key_word}')
        bin_str = bin_str + key_word

    # print(bin_str)
    solve()

    print(f'#{test_case} {ans_str}')
'''
int(num, 16)은 16진수 num을 10진수로 변환,
bin(num)은 10진수 num을 이진수로 변환
format(num, 'spelling')
spelling은 'b', 'o', 'x' 각각 2진수, 10진수, 16진수이다.
num을 해당하는 진수에 맞게 변환

format방식 사용하면 0b같은 접두사 없어지는 대신에 0을 변환하면 '0000' 이 아니라 '0'이 된다.
다른 3자리 내의 2진수도 마찬가지
'''