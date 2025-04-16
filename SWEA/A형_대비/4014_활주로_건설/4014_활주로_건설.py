import sys, pprint
sys.stdin = open('input.txt', 'r')


'''
가로/세로 따로 활주로 세면 됨.
for문 따로 만들기 귀찮으니까 배열 자체를 zip으로 전치행렬로 뒤집으면 된다.
 
경사로의 높이는 항상 1이고, 길이는 테케마다 주어진다.
경사로 지은 인덱스 소수로 바꿔버리기 (2 -> 2.5)
'''

# 이번 행에서 활주로 가능한지 판단
def is_can_slide(i):
    k = 0
    while k != N - X:
        # 만약 현재 높이가 다음 인덱스와 같다면
        if arr[i][k] == arr[i][k+1]:
            k += 1
            continue

        # 만약 현재 높이가 다음 인덱스보다 높다면
        if arr[i][k] > arr[i][k + 1]:
            # 다음인덱스'부터' 경사로의 길이만큼 인덱스 확인, 전부 같아야 경사로 지을 수 있다.
            for x in range(X):
                if arr[i][k + 1 + x] != arr[i][k + 1 + x + 1]:
                    return None

            # 전부 통과한다면, k 값 조정(확인 마친 인덱스 다음 인덱스부터 다시 판단
            k =

        k += 1


def solve(arr):
    cnt = 0
    for i in range(N):
        # arr[i]의 원소들의 값이 모두 같지 않다면, pass
        for j in range(N):
            if arr[i][j] != arr[i][j+1]:
                break
        # 만약 전부 같았다면, 활주로 카운트 + 1
        else:
            cnt += 1

        # 경사로 설치해야 한다면 -----------------------------------
        # 그냥 경사로 길이만큼 idx의 값 구해서 반복하여 비교?
        is_can_slide(i)



        # # arr[i]의 제일 높은 값의 최초 인덱스 구하기
        # peek_v = max(arr[i])
        # sliding_v = peek_v - 1
        # peek_idx = arr[i].index(peek_v)
        #
        # # peek의 좌/우로 한칸씩 값 확인, arr[i][peek]의 값보다 1 낮거나 같은 경우에만 통과
        # for n in (-1, 1):
        #     while 0 <= peek_idx + n <= N-1:
        #         slide_idx = peek_idx + n
        #         if peek_v != arr[i][slide_idx] + 1:
        #             break
        #
        #         if n < 0:
        #             n -= 1
        #         else:
        #             n += 1
        #
        #     #
        #     else:



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



