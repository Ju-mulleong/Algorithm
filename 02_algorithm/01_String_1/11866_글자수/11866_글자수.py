import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

# 문제에서 파이썬의 경우 딕셔너리 사용 가능하다고 함.
for test_case in range(1, 1+T):
    str1 = input()
    str2 = input()

    # str1의 각각의 글자를 key로 하고, 값이 모두 0인 딕셔너리를 만들기
    dict_str1 = {}
    for i in str1:
        dict_str1[i] = 0    # str1에 같은 글자 있어도 상관없다.

    # str2 순회하여 dict_str1의 key와 같으면 그 키의 value +1 하기기
    cnt = 0
    max_cnt = 0

    for i in range(len(str2)):
        if str2[i] in dict_str1.keys():
            dict_str1[str2[i]] += 1

    # dict_str1 의 값중 최대값 출력하기.

    max_value = 0
    for i in dict_str1.values():
        if i > max_value:
            max_value = i

    print(f'#{test_case} {max_value}')