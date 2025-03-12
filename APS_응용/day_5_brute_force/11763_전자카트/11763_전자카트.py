import sys
sys.stdin = open('input.txt', 'r')


'''
순열 만들기, n1, n2, n3, ...m n(n-1)
arr[1][n1]

arr[n1][n2]
arr[n2][n3]
...
arr[nn-2][nn-1]

arr[nn-1][1]
다 합해서 최솟값 구하기
'''


# 배터리 소비량 합산 함수
def sum_function(lst):
    # arr[1][X], arr[Y][1]만 따로 계산하기
    sum_battery = arr[0][lst[0]-1] + arr[lst[-1]-1][0]

    for i in range(N-2):    # 0, 1, 2, ..., N-1
        sum_battery += arr[lst[i]-1][lst[i+1]-1]

    return sum_battery


# 순열 만들기
def dfs(cnt):
    global used, lst, min_v
    # cnt == N-1이면 그때 순열 완성된 것.
    if cnt == N-1:
        # 배터리 소비량 합산 함수
        sum_battery = sum_function(lst)

        # 합산값 최솟값과 비교해서 업데이트
        if min_v > sum_battery:
            min_v = sum_battery
        return

    for i in range(2, N+1):  # 2, 3, 4, ... N
        if used[i] is False:
            # 방문 표시, lst에 더하기
            used[i] = True
            lst.append(i)

            dfs(cnt+1)

            # 원복
            lst.pop()
            used[i] = False


T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [False]*(N+1)    # 0, 1인덱스는 더미, 2부터 시작하니까
    lst = []
    min_v = N*N*100     # 충분히 큰 값
    dfs(0)

    print(f'#{test_case} {min_v}')
