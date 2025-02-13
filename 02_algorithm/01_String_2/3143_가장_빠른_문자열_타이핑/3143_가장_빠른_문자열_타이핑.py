import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):

    text, pattern = map(list, input().split())
    # print(text, pattern)

    # text = ['b', 'a', 'n', 'a', 'n', 'a']
    # pattern = ['b', 'a', 'n', 'a']

    # 슬라이싱?
    # 고전적인 알고리즘

    d = 0
    cnt = 0
    for i in range(len(text)):
        if d > 0:
            d -= 1
            continue
        for j in range(len(pattern)):
            if i + j > len(text)-1:
                cnt += 1    # 패턴 불가하다.
                break

            if pattern[j] != text[i+j]: # 다르다면, i 번째 인덱스는 한 글자 타이핑
                cnt += 1
                # print(cnt)
                break
        else:
            d = len(pattern) - 1    # 이미 다음 시행이라 -1,
            cnt += 1



    print(f'#{test_case} {cnt}')

