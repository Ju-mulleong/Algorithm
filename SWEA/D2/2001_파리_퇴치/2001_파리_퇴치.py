import sys
sys.stdin = open('input.txt', 'r')


'''
M*M 파리채를 한번 내리쳤을때, 최대로 죽일수 있는 파리 개수 구하기
'''

def solve(i, j):
    sum = 0
    for ii in range(i, i+M):
        for jj in range(j, j+M):
            sum += arr[ii][jj]

    return sum


T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # N은 맵 크기, M은 파리채 크기

    arr = [list(map(int, input().split())) for _ in range(N)]
    # 파리 맵 arr
    # print(arr)
    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = solve(i, j)
            max_v = max(max_v, temp)

    print(f'#{test_case} {max_v}')