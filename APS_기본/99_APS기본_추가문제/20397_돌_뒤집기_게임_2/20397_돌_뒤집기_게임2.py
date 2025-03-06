import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N, M = map(int, input().split())
    # 돌의 수 N, 뒤집기 횟수 M

    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())

        arr[i]

'''
?? 문제 이해가 안된다
j가 홀수이면 그럼 어떡해
'''