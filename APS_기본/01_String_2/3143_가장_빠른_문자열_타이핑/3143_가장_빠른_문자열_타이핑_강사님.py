import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def find_t():
    i = 0
    cnt = 0     # cnt를 패턴이 있는 개수로 함.
    # for i in range(N-M+1)을 while로 나타내야됨, 특정 조건하에 i를 바꿔야해서
    while i < N - M + 1:    # 조건식
        for j in range(M):  # 이번 i에서 시작하여서 pattern과 일치하는지 확인
            if text[i + j] != pattern[j]:  # pattren과 다르면, 다음 i로
                break
        else:  # pattern과 일치한다면, 다음 인덱스 설정- 그래서 while 쓰는 것
            '''
            cnt += 1
            i = i+M
            continue
            이거 안되는게 여기서 continue 해버리면 
            이 밑에 i 업데이트하는거 적용 안되고 다음 while 반복으로 넘어간다.
            '''
            i = i + M - 1
            cnt += 1
            continue

        i += 1
    return cnt


for test_case in range(1, 1+T):
    text, pattern = map(list, input().split())

    N = len(text)
    M = len(pattern)

    cnt = find_t()
    ans = N - (M * cnt) + cnt
    '''
    cnt는 text안에 pattern이 있는 개수였다.
    패턴의 길이 M만큼을 한 글자라고 칠 수 있다.(타이핑 한 번)
    이걸 cnt만큼..
    N - (M * cnt)는 pattern아니어서 타이핑한 글자의 수고
    + cnt는 위에서 M만큼을 한 글자라고 친 게 cnt번이니까 + cnt * 1 한 것
    
    '''

    print(f'#{test_case} {ans}')



