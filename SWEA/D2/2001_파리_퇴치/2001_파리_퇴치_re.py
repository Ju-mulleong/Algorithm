import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

'''
N*N크기의 배열에서 M*M의 최댓값 구하기
그냥 DFS
'''

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 현재 좌표가 파리채의 좌상단 꼭짓점
            # print(i, j)
            sum_v = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    sum_v += arr[r][c]
            # 현재까지의 최댓값과 비교
            max_v = max(sum_v, max_v)

    print(f'#{test_case} {max_v}')