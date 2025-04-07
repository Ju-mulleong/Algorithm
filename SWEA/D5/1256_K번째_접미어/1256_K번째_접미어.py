import sys
sys.stdin = open('input.txt', 'r')
import string

T = int(input())


lowercase_lst = list(string.ascii_lowercase)
# print(lowercase_lst)

for test_case in range(1, 1+T):
    K = int(input())
    # 주어진 접미어들 중 사전적 순서로 K번째에 해당하는 접미어 찾기

    str_lst = list(input())
    # print(str_lst)

    # 각 접미어들을 사전적순서로 정렬하여, 그 중 K번째에 해당하는 문자열 출력
    # 존재하지 않는다면, "none" 출력
    temp_str = ''
    temp_lst = []
    for c in str_lst[-1:-len(str_lst)-1:-1]:
        temp_str = c + temp_str
        temp_lst.append(temp_str)

    temp_lst.sort()
    # print(temp_lst)
    try:
        ans = temp_lst[K-1]
    except:
        ans = 'none'
    print(f'#{test_case} {ans}')