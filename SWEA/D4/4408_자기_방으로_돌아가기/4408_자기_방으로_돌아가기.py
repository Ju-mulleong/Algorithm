import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, 1+T):
    N = int(input())
    # 돌아가야 할 학생들의 수 N

    corridor = [0] * 200    # 더미 0 미포함

    for i in range(N):
        a, b = map(int, input().split())
        start = (min(a, b) -1)//2
        end = (max(a, b) -1)//2
        for j in range(start, end+1):
            corridor[j] += 1

    print(f'#{test_case} {max(corridor)}')
