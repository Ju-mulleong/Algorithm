import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):

    pattern = list(input())
    text = list(input())

    # for문과 index만 활용해서 해보자

    M = len(pattern)
    N = len(text)

    ans = 0
    for i in range(N-M+1):      # 마지막 인덱스에서 M 만큼 딱 맞춰서 검색하도록
        for j in range(M):
            if pattern[j] != text[i+j]:
                break
        else:
            ans = 1

    print(f'#{test_case} {ans}')
