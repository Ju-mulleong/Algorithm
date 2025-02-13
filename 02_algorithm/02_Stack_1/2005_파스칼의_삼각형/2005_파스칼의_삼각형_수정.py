import sys
import pprint

sys.stdin = open('input.txt', 'r')

T = int(input())

def f(N):
    lst = [[1], [1, 1]]
    for i in range(3, N+1):
        lst.append([0]*i)
    # print(lst)
    for i in range(2, N):
        for j in range(i+1):
            if j == 0 or j == i:    # 이번 반복의 첫 인덱스거나 마지막 인덱스 일때
                lst[i][j] = 1

            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    return lst


for test_case in range(1, 1+T):
    N = int(input())

    # arr = [[1], [1, 1]]

    if N == 1:
        ans = [[1]]
    elif N == 2:
        ans = [[1], [1, 1]]
    else:
        ans = f(N)

    print(f'#{test_case}')
    for i in ans:
        for j in i:
            print(j, end=' ')
        print()







