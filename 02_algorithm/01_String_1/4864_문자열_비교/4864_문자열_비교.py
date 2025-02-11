import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # 테스트 케이스의 개수 T

for test_case in range(1, 1+T):
    str1 = input()
    str2 = input()

    # str2에 str1이 존재하면 1, 그렇지 않으면 0 출력

    '''
    1. if문으로 str2 글자마다 str1길이만큼 반복해서 탐색
        in 쓰면 ?
    '''

    ans = 0
    for i in range(len(str2)):
        if str2[i] == str1[0]:  # 만약 첫 글자 같은 것 발견하면
            if str2[i:i + len(str1)] == str1:   # 첫 글자 인덱스에서 str1길이만큼의 인덱스 '미만'까지 슬라이싱
                ans = 1
                break

    print(f'#{test_case} {ans}')