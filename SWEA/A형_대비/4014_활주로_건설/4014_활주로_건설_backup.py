import sys, pprint
sys.stdin = open('input.txt', 'r')


'''
가로/세로 따로 활주로 세면 됨.
for문 따로 만들기 귀찮으니까 배열 자체를 zip으로 전치행렬로 뒤집으면 된다.
 
경사로의 높이는 항상 1이고, 길이는 테케마다 주어진다.
경사로 지은 인덱스 소수로 바꿔버리기 (2 -> 2.5)

'''

# 이번 행에서 활주로 가능한지 판단
def is_can_slide(arr, i):
    global cnt
    slide_up_cnt = 0
    slide_down_cnt = 0
    j = 0
    X_cnt = 0
    while j < N-1:
        # 현재 값이랑 다음 값이랑 같으면, slide_up_cnt 하기 시작
        if arr[i][j] == arr[i][j + 1]:
            slide_up_cnt += 1
            if X_cnt > 0:
                X_cnt -= 1
        # 현재 값이 다음 값보다 1작다면
        # 지금까지 센 slide_cnt가 X보다 크거나 같으면 가능하다.
        elif arr[i][j] == arr[i][j + 1] + 1:
            # 올라가는 경사로 설치 가능 판단
            # 불가능하다면, 이번 행에서 활주로 설치 불가
            # 내려가는 경사로 세운 뒤에, X_cnt 가 양수이면 불가능
            if slide_up_cnt < X or X_cnt > 0:
                return

            # 경사로 설치 가능하다면, 지금까지의 slide_cnt 초기화
            slide_up_cnt = 0
            X_cnt = 0

        # 현재 값이 다음 값보다 1 크다면 내려가는 경사로 설치 가능한지 판단
        elif arr[i][j] == arr[i][j+1] - 1:
            # 다음값부터 다시 slide_cnt 세기
            for x in range(X):  # 0 ~ X-1
                # 정상인덱스인지 확인, 비정상인덱스면 return
                if j+1+x+1 < 0 or j+1+x+1 >= N:
                    return

                if arr[i][j+1+x] != arr[i][j+1+x+1]:
                    return
            # X만큼 slide_cnt 셀 수 있다면, 거기까지 경사로 세우고 경사로 세운 다음 인덱스로 넘어가기
            # 내려가는 경사로 세운 다음 인덱스부터 경사로 길이만큼 다시 확인
            # 뭘 확인: arr[i][j+1+X] 보다 큰 값이면 안된다. 올라가는 경사로 못 세움.
            X_cnt = X
            j = j+1+X   # 어차피 밑에서 다시 1 더한다.

        j += 1

    # while문 다 통과하면, cnt += 1
    cnt += 1


def solve():
    for i in range(N):

        # 그냥 경사로 길이만큼 idx의 값 구해서 반복하여 비교?
        is_can_slide(arr, i)
        is_can_slide(arr_zip, i)


T = int(input())

for test_case in range(1, 1+T):
    # 지도의 한 변의 크기 N, 경사로의 길이 X
    N, X = map(int, input().split())

    # N*N 지형
    arr = [list(map(int, input().split())) for _ in range(N)]

    # arr의 전치행렬
    arr_zip = [list(row) for row in zip(*arr)]
    # pprint.pprint(arr)
    # pprint.pprint(arr_zip)

    cnt = 0
    solve()
    print(f'#{test_case} {cnt}')


