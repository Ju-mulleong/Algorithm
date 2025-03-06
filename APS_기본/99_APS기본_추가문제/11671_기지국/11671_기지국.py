import sys
sys.stdin = open('input.txt', 'r')

'''
델타 응용 쓰는거
그냥 행 우선탐색으로 기지국 위치 찾으면 
A, B, C 일때 각각 규칙만큼 탐색하여
    만약 H가 있으면 H를 X로 바꾼다
    없으면 pass
다 끝난 다음에 전체 2차원배열에서 H개수 찾기
    count써도 되나?
    쓰는 연습 하자
'''


def cover_home(Alphabet):
    global arr      # arr 전역변수 처리!!
    if Alphabet == 'A':
        num = 1
    elif Alphabet == 'B':
        num = 2
    elif Alphabet == 'C':
        num = 3

    di = [0, -1, 0, 1]
    dj = [1, 0, -1, 0]
    for d in range(4):
        for k in range(1, num+1):
            ni = i +di[d]*k
            nj = j +dj[d]*k
            if 0 <= ni <= N-1 and 0 <= nj <= N-1:   # 정상인덱스라면
                if arr[ni][nj] == 'H':
                    arr[ni][nj] = 'O'     # 기지국이 커버하는 집은 'O'로 표시


T = int(input())


for test_case in range(1, 1+T):
    N = int(input())    # N*N의 배열

    arr = [list(input()) for _ in range(N)]
    # print(arr)

    for i in range(N):
        for j in range(N):
            if arr[i][j] in 'ABC':
                cover_home(arr[i][j])

    # 기지국 커버 표시 끝났으면 'H' 세어서 출력
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{test_case} {cnt}')